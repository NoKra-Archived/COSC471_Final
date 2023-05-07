import pygame
from OpenGL.GL import *

class PrintedObject:
    def __init__(self):
        self.points = []
        self.z_position = 0


    def update_object_frame(self):
        self.__build_printed_object()

    def __build_printed_object(self):
        glPointSize(3)
        glBegin(GL_POINTS)
        for point in self.points:
            glColor3d(0.0, 0.5, 0.7)
            glVertex3d(point[0], point[1], -point[2] + self.z_position)
        glEnd()

    def insert_point(self, new_point, z_position):
        self.z_position = z_position
        self.points.append(new_point)
