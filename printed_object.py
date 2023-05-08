from OpenGL.GL import *
import random

class PrintedObject:
    def __init__(self, printer):
        self.printer = printer
        self.points = []
        self.z_position = 0


    def update_object_frame(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self.__build_printed_object()

    def __generate_layer_color(self):
        z_position = self.printer.get_nozzle_position()[1]
        random.seed(z_position * 4)
        red = random.random()
        random.seed(z_position * 9)
        green = random.random()
        random.seed(z_position * 13)
        blue = random.random()
        return red, green, blue

    def __build_printed_object(self):
        glPointSize(3)
        glBegin(GL_POINTS)
        for point in self.points:
            #glColor3d(0.0, 0.5, 0.7)
            glColor3d(point[1][0], point[1][1], point[1][2])
            glVertex3d(point[0][0], point[0][1], -point[0][2] + self.z_position)
        glEnd()

    def insert_point(self):
        self.z_position = self.printer.get_z_position()
        self.points.append((self.printer.get_nozzle_position(), self.__generate_layer_color()))
