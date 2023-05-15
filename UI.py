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
    pt = int(pt) * sr
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
    if (pt > 59):
        pm = int(pt / 60)
        ps = int(pt % 60)
        if (pm < 10 and ps < 10):
            t5w, t5h = drawUIText(
                10, h - (30 + t1h + t2h + t3h + t4h), 16, "Time Spent Printing: 0" + pm.__str__() + ":0" + ps.__str__())
        if (pm < 10 and ps >= 10):
            t5w, t5h = drawUIText(
                10, h - (30 + t1h + t2h + t3h + t4h), 16, "Time Spent Printing: 0" + pm.__str__() + ":" + ps.__str__())
        if (pm >= 10 and ps < 10):
            t5w, t5h = drawUIText(
                10, h - (30 + t1h + t2h + t3h + t4h), 16, "Time Spent Printing: " + pm.__str__() + ":0" + ps.__str__())
        if (pm >= 10 and ps >= 10):
            t5w, t5h = drawUIText(
                10, h - (30 + t1h + t2h + t3h + t4h), 16, "Time Spent Printing: " + pm.__str__() + ":" + ps.__str__())
    else:
        if (pt < 10):
            t5w, t5h = drawUIText(
                10, h - (30 + t1h + t2h + t3h + t4h), 16, "Time Spent Printing: 00:0" + pt.__str__())
        else:
            t5w, t5h = drawUIText(
                10, h - (30 + t1h + t2h + t3h + t4h), 16, "Time Spent Printing: 00:" + pt.__str__())


def drawHelpMenu():
    pass
