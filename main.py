import numpy
import UI
import pygame
import random

from printer import Printer
from camera import Camera
from g_code import GCode
from printed_object import PrintedObject


def main():
    pygame.init()
    sim_rate = 1
    # adjust tick_rate / adjust_feed_rate for a good balance of performance /clarity
    tick_rate = 3

    camera = Camera()
    printer = Printer(tick_rate, sim_rate)
    print_object = PrintedObject(printer)
    g_code = GCode(printer, "sample_2.txt")

    points = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    printer.start_print(g_code)

            camera.update_camera_event(event)
            printer.update_printer_event(event)

        if not printer.movement_queue.empty():
            should_extrude = printer.move_printer()
            if should_extrude:
                print_object.insert_point()
                points += 1
                # print("Points: %d" % points)
        elif not g_code.command_queue.empty():
            g_code.process_g_code()

        camera.update_camera_frame(pygame.key.get_pressed())
        print_object.update_object_frame()
        printer.update_printer_frame()
        UI.drawUI(camera.get_size(), printer, sim_rate)

        pygame.display.flip()
        pygame.time.wait(tick_rate)


main()
