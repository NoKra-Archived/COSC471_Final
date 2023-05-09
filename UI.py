import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def drawUIText(x, y, font_size, textString):
    font = pygame.font.Font("Fonts/FiraCode-VF.ttf", font_size)
    render = font.render(
        textString, True, (255, 255, 255, 255), (0, 0, 0, 0)).convert_alpha()
    textData = pygame.image.tostring(render, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(render.get_width(), render.get_height(),
                 GL_RGBA, GL_UNSIGNED_BYTE, textData)
    return render.get_width(), render.get_height()


def drawUI(size):
    w, h = size
    t1w, t1h = drawUIText(
        w/2, h - (30), 16, "Head Speed: 0 m/s.")
    t2w, t2h = drawUIText(
        w/2, h - (30 + t1h), 16, "Extrusion Speed: 0 m/s.")
    t3w, t3h = drawUIText(
        w/2, h - (30 + t1h + t2h), 16, "Extruded Length: 100 m.")
