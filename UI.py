import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import time


def drawUIText(x, y, font_size, textString):
    font = pygame.font.Font("Fonts/FiraCode-VF.ttf", font_size)
    render = font.render(
        textString, True, (255, 255, 255, 255), (0, 0, 0, 0)).convert_alpha()
    textData = pygame.image.tostring(render, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(render.get_width(), render.get_height(),
                 GL_RGBA, GL_UNSIGNED_BYTE, textData)
    return render.get_width(), render.get_height()


def drawUI(size, printer, sr, pt):
    w, h = size
    pm = 0
    ps = 0
    t1w, t1h = drawUIText(
        10, h - (30), 16, "Layer " + printer.current_layer.__str__() + ".")
    t2w, t2h = drawUIText(
        10, h - (30 + t1h), 16, "Simulation Speed: " + sr.__str__() + "x")
    t3w, t3h = drawUIText(
        10, h - (30 + t1h + t2h), 16, "Current Extrusion Speed: " + printer.get_extrusion_speed().__str__() + " mm/min.")
    t4w, t4h = drawUIText(
        10, h - (30 + t1h + t2h + t3h), 16, "Extruded Length: " + printer.get_total_extruded().__str__() + " mm^3.")
    t5w, t5h = drawUIText(
        10, h - (30 + t1h + t2h + t3h + t4h), 16, "Time Spent Printing: " + format_print_time(pt))


def format_print_time(print_time):
    seconds = int(print_time % 60)
    minutes = int((print_time % 3600) / 60)
    hours = int(print_time / 3600)
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

def drawHelpMenu():
    pass
