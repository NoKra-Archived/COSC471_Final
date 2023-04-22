import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from head import PrinterHead

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

    z_tran_start = -15.0
    y_tran_start = 0.5
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, y_tran_start, z_tran_start)

    x_rot_current = 0
    y_rot_current = 0


    z_tran_current = z_tran_start
    y_tran_current = y_tran_start

    rot_rate = 1
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
                    glTranslatef(0.0, y_tran_start, z_tran_start)
                    x_rot_current = 0
                    y_rot_current = 0
            # Handles zoom in and zoom out (for now, only works when y rotation is 0)
            if event.type == pygame.MOUSEWHEEL:
                abs_x_rot = abs(x_rot_current)
                if 0 <= abs_x_rot <= 89 or 181 <= abs_x_rot <= 269:
                    modded_x = abs_x_rot % 90
                    quadrant = 1 if abs_x_rot <= 90 else -1
                    if event.y == -1:
                        glTranslatef(quadrant * (modded_x / 90), 0, quadrant * (-(90 - modded_x) / 90))
                    if event.y == 1:
                        glTranslatef(quadrant * (-modded_x / 90), 0, quadrant * ((90 - modded_x) / 90))
                elif abs_x_rot == 90:
                    if event.y == -1:
                        glTranslatef(1.0, 0.0, 0.0)
                    if event.y == 1:
                        glTranslatef(-1.0, 0.0, 0.0)
                elif 91 <= abs_x_rot <= 179 or 271 <= abs_x_rot <= 359:
                    modded_x = abs_x_rot % 90
                    quadrant = 1 if abs_x_rot < 180 else -1
                    if event.y == -1:
                        glTranslatef(quadrant * ((90 - modded_x) / 90), 0, quadrant * (modded_x / 90))
                    if event.y == 1:
                        glTranslatef(quadrant * (-(90 - modded_x) / 90), 0, quadrant * (-modded_x / 90))
                elif abs_x_rot == 180:
                    if event.y == -1:
                        glTranslatef(0.0, 0.0, 1.0)
                    if event.y == 1:
                        glTranslatef(0.0, 0.0, -1.0)

        # Directional key rotation
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            glRotatef(-rot_rate, 0, 1, 0)
            x_rot_current -= rot_rate
            print("X: %d" % x_rot_current)
        if pressed_key[pygame.K_RIGHT]:
            glRotatef(rot_rate, 0, 1, 0)
            x_rot_current += rot_rate
            print("X: %d" % x_rot_current)
        if pressed_key[pygame.K_DOWN]:
            #if y_rot_current < 180:
                glRotatef(rot_rate, 1, 0, 0)
                y_rot_current += rot_rate
                print("Y: %d" % y_rot_current)
        if pressed_key[pygame.K_UP]:
            #if y_rot_current >= 0:
                glRotatef(-rot_rate, 1, 0, 0)
                y_rot_current -= rot_rate
                print("Y: %d" % y_rot_current)

        if x_rot_current >= 360:
            x_rot_current = 0
        if x_rot_current < 0:
            x_rot_current = 359
        if y_rot_current >= 360 or y_rot_current <= -360:
            y_rot_current = 0

        """ Mouse rotation implementation, fine tuning with keys
        left, middle, right = pygame.mouse.get_pressed()
        x_mouse, y_mouse = pygame.mouse.get_rel()
        if left:
            x_rot_current += x_mouse
            y_rot_current += y_mouse
            glRotatef(1 * (x_mouse * rotation_rate), 0, 1, 0)
            glRotatef(1 * (y_mouse * rotation_rate), 0, 0, 1)
            print("[%d , %d]" % (x_rot_current, y_rot_current))
        """

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
