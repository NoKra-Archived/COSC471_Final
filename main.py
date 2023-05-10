import pygame

from printer import Printer
from camera import Camera
from g_code import GCode
from printed_object import PrintedObject


def main():
    pygame.init()
    display = (1600, 1000)  # screen size
    tick_rate = 1  # keep this at one, control speed with adjust_movement_rate in printer
    camera = Camera(display)
    printer = Printer(tick_rate)
    print_object = PrintedObject(printer)
    g_code = GCode(printer, "astro.txt")  # just change a .gcode file to .txt extension

    is_printing = False  # locks printing if printing is already in progress
    is_paused = False  #
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and not is_printing:
                    printer.start_print(g_code)
                    is_printing = True
                if event.key == pygame.K_z:
                    is_paused = not is_paused

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

        camera.update_camera_frame(pygame.key.get_pressed())
        print_object.update_object_frame()
        printer.update_printer_frame()

        pygame.display.flip()
        pygame.time.wait(tick_rate)


main()
