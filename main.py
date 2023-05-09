import numpy
import UI
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    pygame.init()
    display = pygame.display.set_mode(
        (0, 0), flags=DOUBLEBUF | OPENGL | RESIZABLE)

    UI.drawUI(display)


main()
