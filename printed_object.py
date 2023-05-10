from OpenGL.GL import *
import random

class PrintedObject:
    def __init__(self, printer):
        self.printer = printer
        self.temporary_points = []
        self.permanent_line_points = []
        self.z_position = 0


    def update_object_frame(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self.__build_permanent_printed_object()
        self.__build_temporary_printed_object()

    def __generate_layer_color(self):
        z_position = self.printer.get_nozzle_position()[1]
        random.seed(z_position * 4)
        red = random.random()
        random.seed(z_position * 9)
        green = random.random()
        random.seed(z_position * 13)
        blue = random.random()
        return red, green, blue

    def __build_permanent_printed_object(self):
        glLineWidth(4)
        glBegin(GL_LINES)
        for point in self.permanent_line_points:
            glColor3d(point[1][0], point[1][1], point[1][2])
            glVertex3f(point[0][0], point[0][1], -point[0][2] + self.z_position)
        glEnd()

    def __build_temporary_printed_object(self):
        glPointSize(4)
        glBegin(GL_POINTS)
        for point in self.temporary_points:
            glColor3d(point[1][0], point[1][1], point[1][2])
            glVertex3d(point[0][0], point[0][1], -point[0][2] + self.z_position)
        glEnd()

    def insert_permanent_point(self):
        self.z_position = self.printer.get_z_position()
        self.permanent_line_points.append((self.printer.get_nozzle_position(), self.__generate_layer_color()))

    def insert_temporary_point(self):
        self.z_position = self.printer.get_z_position()
        self.temporary_points.append((self.printer.get_nozzle_position(), self.__generate_layer_color()))

    def erase_temporary_points(self):
        self.temporary_points.clear()
