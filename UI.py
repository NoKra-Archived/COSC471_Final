import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def drawUIText(x, y, textString):
    font = pygame.font.Font("Fonts/FiraCode-VF.ttf", 16)
    render = font.render(textString, True, (255, 255, 255))
    textData = pygame.image.tostring(render, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(render.get_width(), render.get_height(),
                 GL_RGBA, GL_UNSIGNED_BYTE, textData)
    return render
