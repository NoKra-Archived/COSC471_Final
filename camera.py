import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Camera:
    def __init__(self):
        display = pygame.display.set_mode((0, 0), DOUBLEBUF | OPENGL)

        self.display_dimensions = display.get_size()



        self.init_fov_y = 45
        self.init_z_near = 0.1
        self.init_z_far = 3000

        gluPerspective(self.init_fov_y,
                       (self.display_dimensions[0]/self.display_dimensions[1]),
                       self.init_z_near, self.init_z_far)

        self.init_x_translate = 0
        self.init_y_translate = 100
        self.init_z_translate = -1000

        glTranslatef(self.init_x_translate,
                     self.init_y_translate, self.init_z_translate)

        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0
        self.rotation_rate = 1
        self.zoom_rate = 20
        self.pan_rate = 5

    def update_camera_event(self, event):
        self.__zoom_event(event)
        self.__reset_camera_event(event)

    # there's definitely a better way to do this, way too many if statements
    def update_camera_frame(self, pressed_key):
        self.__x_rotation_pressed(pressed_key)
        self.__y_rotation_pressed(pressed_key)
        self.__panning_pressed(pressed_key)

    def __reset_camera_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                glLoadIdentity()
                gluPerspective(self.init_fov_y,
                               (self.display_dimensions[0] /
                                self.display_dimensions[1]),
                               self.init_z_near, self.init_z_far)
                glTranslatef(self.init_x_translate,
                             self.init_y_translate, self.init_z_translate)
                self.rotation_x = 0
                self.rotation_y = 0
                self.rotation_z = 0

    def __zoom_event(self, event):
        if event.type == pygame.MOUSEWHEEL:
            abs_x_rot = abs(self.rotation_x)
            if 0 <= abs_x_rot <= 89 or 181 <= abs_x_rot <= 269:
                modded_x = abs_x_rot % 90
                quadrant = self.zoom_rate if abs_x_rot <= 90 else -self.zoom_rate
                if event.y == -1:
                    glTranslatef(quadrant * (modded_x / 90), 0,
                                 quadrant * (-(90 - modded_x) / 90))
                if event.y == 1:
                    glTranslatef(quadrant * (-modded_x / 90), 0,
                                 quadrant * ((90 - modded_x) / 90))
            elif abs_x_rot == 90:
                if event.y == -1:
                    glTranslatef(self.zoom_rate, 0.0, 0.0)
                if event.y == 1:
                    glTranslatef(-self.zoom_rate, 0.0, 0.0)
            elif 91 <= abs_x_rot <= 179 or 271 <= abs_x_rot <= 359:
                modded_x = abs_x_rot % 90
                quadrant = self.zoom_rate if abs_x_rot < 180 else -self.zoom_rate
                if event.y == -1:
                    glTranslatef(quadrant * ((90 - modded_x) / 90),
                                 0, quadrant * (modded_x / 90))
                if event.y == 1:
                    glTranslatef(quadrant * (-(90 - modded_x) / 90),
                                 0, quadrant * (-modded_x / 90))
            elif abs_x_rot == 180:
                if event.y == -1:
                    glTranslatef(0.0, 0.0, self.zoom_rate)
                if event.y == 1:
                    glTranslatef(0.0, 0.0, -self.zoom_rate)

    def __x_rotation_pressed(self, pressed_key):
        if pressed_key[pygame.K_LEFT]:
            glRotatef(-self.rotation_rate, 0, 1, 0)
            self.rotation_x -= self.rotation_rate
            if self.rotation_x < 0:
                self.rotation_x = 360
            print("X: %d" % self.rotation_x)
        elif pressed_key[pygame.K_RIGHT]:
            glRotatef(self.rotation_rate, 0, 1, 0)
            self.rotation_x += self.rotation_rate
            if self.rotation_x >= 360:
                self.rotation_x = 0
            print("X: %d" % self.rotation_x)

    def __y_rotation_pressed(self, pressed_key):
        if pressed_key[pygame.K_DOWN]:
            glRotatef(self.rotation_rate, 1, 0, 0)
            self.rotation_y += self.rotation_rate
            if self.rotation_y >= 360:
                self.rotation_y = 0
            print("Y: %d" % self.rotation_y)
        elif pressed_key[pygame.K_UP]:
            glRotatef(-self.rotation_rate, 1, 0, 0)
            self.rotation_y -= self.rotation_rate
            if self.rotation_y < 0:
                self.rotation_y = 360
            print("Y: %d" % self.rotation_y)

    def __panning_pressed(self, pressed_key):
        if pressed_key[pygame.K_w]:
            glTranslatef(0, -self.pan_rate, 0)
        elif pressed_key[pygame.K_s]:
            glTranslatef(0, self.pan_rate, 0)
        elif pressed_key[pygame.K_a]:
            glTranslatef(-self.pan_rate, 0, 0)
        elif pressed_key[pygame.K_d]:
            glTranslatef(self.pan_rate, 0, 0)
        elif pressed_key[pygame.K_q]:
            glTranslatef(0, 0, -self.pan_rate)
        elif pressed_key[pygame.K_e]:
            glTranslatef(0, 0, self.pan_rate)

    def get_size(self):
        return (self.display_dimensions[0], self.display_dimensions[1])
