from OpenGL.GL import *
from OpenGL.GLU import *

from head import PrinterHead
from rail_horizontal import HorizontalRail
from rail_vertical import VerticalRail
from plate import Plate

class Printer:

    def __init__(self):
        self.dimension = 75


    def update_printer(self, current_x, current_y, current_z):
        self.__build_printer_head(current_x, current_y)
        self.__build_horizontal_rail(current_y)
        self.__build_vertical_rail()
        self.__build_plate(current_z)

    def __build_printer_head(self, current_x, current_y):
        glBegin(GL_LINES)
        head = PrinterHead(self.dimension, current_x, current_y)
        for part in head.all_parts:
            for edge in part[1]:
                for vertex in edge:
                    glVertex3fv(part[0][vertex])

        glEnd()

    def __build_horizontal_rail(self, current_y):
        glBegin(GL_LINES)
        horizontal_rail = HorizontalRail(self.dimension, current_y)
        for part in horizontal_rail.all_parts:
            for edge in part[1]:
                for vertex in edge:
                    glVertex3fv(part[0][vertex])

        glEnd()

    def __build_vertical_rail(self):
        glBegin(GL_LINES)
        vertical_rail = VerticalRail(self.dimension)
        for part in vertical_rail.all_parts:
            for edge in part[1]:
                for vertex in edge:
                    glVertex3fv(part[0][vertex])

        glEnd()

    def __build_plate(self, current_z):
        glBegin(GL_LINES)
        plate = Plate(self.dimension, current_z)
        for part in plate.all_parts:
            for edge in part[1]:
                for vertex in edge:
                    glVertex3fv(part[0][vertex])

        glEnd()