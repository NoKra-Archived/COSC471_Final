import numpy
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    pygame.display.set_mode((0, 0), flags=DOUBLEBUF | OPENGL | RESIZABLE)

    displayInfo = pygame.display.Info()

    gluPerspective(45, ((displayInfo.current_w) /
                        (displayInfo.current_h - 30)), 0.1, 50.0)

    initialTranslate = True
    frame = 0
    while True:
        print("Frame " + frame.__str__())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if initialTranslate:
            glTranslatef(0.0, 0.0, -5)
            initialTranslate = False
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        frame += 1
        pygame.time.wait(10)


main()
