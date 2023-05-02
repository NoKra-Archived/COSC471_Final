import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def drawUIText(x, y, font_size, dh, dw, textString):
    font = pygame.font.Font("Fonts/FiraCode-VF.ttf", font_size)
    render = font.render(
        textString, True, (255, 255, 255, 255), (0, 0, 0, 0)).convert_alpha()
    textData = pygame.image.tostring(render, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(render.get_width(), render.get_height(),
                 GL_RGBA, GL_UNSIGNED_BYTE, textData)
    return render.get_width(), render.get_height()
