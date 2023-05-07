import pygame

from printer import Printer
from camera import Camera


def main():
    pygame.init()
    display = (800, 600)

    camera = Camera(display)
    printer = Printer()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            camera.update_camera_event(event)
            printer.update_printer_event(event)

        if not printer.command_queue.empty():
            printer.move_printer(printer.command_queue.get())

        camera.update_camera_frame(pygame.key.get_pressed())
        printer.update_printer_frame()

        pygame.display.flip()
        pygame.time.wait(10)


main()
