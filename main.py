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
    (2, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    x_current = 0
    y_current = 0

    rotation_rate = 0.3
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # Resets the camera to it's origin
                if event.key == pygame.K_x:
                    glLoadIdentity()
                    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                    glTranslatef(0.0, 0.0, -5)
                    x_current = 0
                    y_current = 0
                if event.key == pygame.K_f:
                    gluLookAt(0, -3, 0, 0, 0, 0, -1, 0, 0)


        # Directional key rotation
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            glRotatef(-1, 0, 1, 0)
            x_current += -1
            print("X: %d" % x_current)
        if pressed_key[pygame.K_RIGHT]:
            glRotatef(1, 0, 1, 0)
            x_current += 1
            print("X: %d" % x_current)
        if pressed_key[pygame.K_DOWN]:
            glRotatef(1, y_current, 0, 0)
            y_current += 1
            print("Y: %d" % y_current)
        if pressed_key[pygame.K_UP]:
            glRotatef(-1, y_current, 0, 0)
            y_current -= 1
            print("Y: %d" % y_current)

        if x_current > 360 or x_current < -360:
            x_current = 0
        if y_current > 360 or y_current < -360:
            y_current = 0

        """ Mouse rotation implementation, fine tuning with keys
        left, middle, right = pygame.mouse.get_pressed()
        x_mouse, y_mouse = pygame.mouse.get_rel()
        if left:
            x_current += x_mouse
            y_current += y_mouse
            glRotatef(1 * (x_mouse * rotation_rate), 0, 1, 0)
            glRotatef(1 * (y_mouse * rotation_rate), 0, 0, 1)
            print("[%d , %d]" % (x_current, y_current))
        """

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()