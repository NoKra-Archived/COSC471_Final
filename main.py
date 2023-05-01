import numpy
import UI
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
    display = pygame.display.set_mode(
        (0, 0), flags=DOUBLEBUF | OPENGL | RESIZABLE)

    frame = 0
    w, h = display.get_size()
    while True:
        print("Frame " + frame.__str__())
        glViewport(0, int(h / 4), int(w / 2),
                   int((h / 2) - 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == VIDEOEXPOSE:
                print("Exposed!")
            elif event.type == VIDEORESIZE:
                print("Resized!")
                glLoadIdentity()
                try:
                    w, h = event.dict['size']
                except:
                    print("Failed to find event.dict['size']")
                    w, h = display.get_size()
                gluPerspective(45, (w / (h - 30)), 0.1, 50.0)
                glTranslatef(0.0, 0.0, -5)

        print("Screen: w = " + w.__str__() + ", h = " + h.__str__())
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)
        Cube()
        t1w, t1h = UI.drawUIText(
            w/2, h - 30, 16, h, w, "Frame " + frame.__str__())
        t2w, t2h = UI.drawUIText(
            w/2, h - (30 + t1h), 16, h, w, "Head Speed: 0 m/s.")
        t3w, t3h = UI.drawUIText(
            w/2, h - (30 + t1h + t2h), 16, h, w, "Extrusion Speed: 0 m/s.")
        t4w, t4h = UI.drawUIText(
            w/2, h - (30 + t1h + t2h + t3h), 16, h, w, "Extruded Length: 100 m.")
        pygame.display.flip()
        frame += 1
        pygame.time.wait(10)


main()
