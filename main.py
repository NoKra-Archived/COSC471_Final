import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from head import PrinterHead

head_vertices = (
    # Main box start
    (1, -3, -3),  # right bottom back 0
    (1, 2, -3),  # right top back 1
    (-1, 2, -3),  # left top back 2
    (-1, -3, -3),  # left bottom back 3
    (1, -3, 2),  # right bottom front 4
    (1, 2, 2),  # right top front 5
    (-1, -3, 2),  # left bottom front 6
    (-1, 2, 2),  # left top front 7
    # Main box end
    # Fan box start
    (-1, 1, 1),  # top front attach 8
    (-1, 1, -2),  # top back attach 9
    (-1, -2, 1),  # bottom front attach 10
    (-1, -2, -2),  # bottom back attach 11
    (-2, 1, 1),  # top front box 12
    (-2, 1, -2),  # top back box 13
    (-2, -2, 1),  # bottom front box 14
    (-2, -2, -2),  # bottom back box 15
    # Fan box end
    # Nozzle stem start
    (-0.5, -3, 1),  # front left attach 16
    (0.5, -3, 1),  # front right attach 17
    (-0.5, -3, 0),  # back left attach 18
    (0.5, -3, 0),  # back right attach 19
    (-0.5, -3.5, 1),  # front left stem 20
    (0.5, -3.5, 1),  # front right stem 21
    (-0.5, -3.5, 0),  # back left stem 22
    (0.5, -3.5, 0),  # back right stem 23
    # Nozzle stem end
    # Nozzle head start
    (-1, -3.5, 2),  # front left top 24
    (1, -3.5, 2),  # front right top 25
    (-1, -3.5, -2),  # back left top 26
    (1, -3.5, -2)  # back right top 27
    )

head_edges = (
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
    (5,7),
    (7, 8),
    (2, 9),
    (6, 10),
    (3, 11),
    (8, 9),
    (8, 10),
    (10, 11),
    (9, 11),
    (8, 12),
    (9, 13),
    (10, 14),
    (11, 15),
    (12, 13),
    (12, 14),
    (14, 15),
    (13, 15),
    (6, 16),
    (4, 17),
    (3, 18),
    (0, 19),
    (16, 17),
    (17, 19),
    (16, 18),
    (18, 19),
    (16, 20),
    (17, 21),
    (18, 22),
    (19, 23),
    (20, 21),
    (20, 22),
    (21, 23),
    (22, 23),
    (20, 24),
    (21, 25),
    (22, 26),
    (23, 27),
    (24, 25),
    (24, 26),
    (25, 27),
    (26, 27)
    )


def Cube():
    glBegin(GL_LINES)
    head = PrinterHead(1, 5, 5)
    for part in head.all_parts:
        for edge in part[1]:
            for vertex in edge:
                glVertex3fv(part[0][vertex])

    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    z_original = -12.0
    y_original = 0.5
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, y_original, z_original)

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
                    glTranslatef(0.0, y_original, z_original)
                    x_current = 0
                    y_current = 0


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
            #if y_current < 180:
                glRotatef(1, 1, 0, 0)
                y_current += 1
                print("Y: %d" % y_current)
        if pressed_key[pygame.K_UP]:
            #if y_current >= 0:
                glRotatef(-1, 1, 0, 0)
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