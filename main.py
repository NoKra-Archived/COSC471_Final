import UI
import pygame
import time

from printer import Printer
from camera import Camera
from g_code import GCode
from printed_object import PrintedObject


def main():
    global printing_start_time
    global printing_time
    printing_start_time = 0
    printing_time = 0
    pygame.init()
    sim_rate = 5
    # adjust tick_rate / adjust_feed_rate for a good balance of performance /clarity
    tick_rate = 1

    camera = Camera()
    printer = Printer(tick_rate, sim_rate)
    print_object = PrintedObject(printer)
    # just change a .gcode file to .txt extension
    g_code = GCode(printer, "astro.txt")

    is_printing = False  # locks printing if printing is already in progress
    is_paused = False  #
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and not is_printing:
                    printing_start_time = time.time()
                    printer.start_print(g_code)
                    is_printing = True
                if event.key == pygame.K_z:
                    is_paused = not is_paused
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            camera.update_camera_event(event)

        if not printer.movement_queue.empty():
            insert_status = printer.move_printer()
            if insert_status[1]:
                print_object.insert_temporary_point()
            if insert_status[0]:
                print_object.insert_permanent_point()
                print_object.erase_temporary_points()
        elif not g_code.command_queue.empty() and not is_paused:
            g_code.process_g_code()
        else:
            is_printing = False

        if is_printing:
            printing_time = time.time() - printing_start_time
        camera.update_camera_frame(pygame.key.get_pressed())
        print_object.update_object_frame()
        printer.update_printer_frame()
        UI.drawUI(camera.get_size(), printer, sim_rate, printing_time)

        pygame.display.flip()
        pygame.time.wait(tick_rate)


main()
