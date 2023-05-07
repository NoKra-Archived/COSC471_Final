import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from queue import Queue
import math

from head import PrinterHead
from rail_horizontal import HorizontalRail
from rail_vertical import VerticalRail
from plate import Plate

class Printer:

    def __init__(self):
        self.__dimension = 75  # 75 dimension should create the 180mm print plate size (1 to 1)
        self.__bed_level = -self.__dimension * 4.5
        self.__plate_x_zero = 0
        self.__plate_z_zero = 0
        self.__x_offset = self.__dimension * 2.66  # handles the x shift for the entire printer in relation to the camera

        self.__model_x_position = 0
        self.__model_y_position = 0  # model positions account for the 3D model of the printer
        self.__model_z_position = 0
        # The 3D model of the printer shouldn't be used as the position for the g-code instructions
        self.__print_x_position = 0
        self.__print_y_position = 0  # print positions account for position in 3D space of the printer head
        self.__print_z_position = 0

        self.__movement_rate = 10

        self.command_queue = Queue(maxsize= 0)
        self.nozzle_position = (0, 0, 0)  # updated whenever the head is built

    def update_printer_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.__manual_test(event)
            self.__reset_printer(event)

    def move_printer(self, translation):
        self.__model_x_position += translation[0]
        self.__model_y_position += translation[1]
        self.__model_z_position += translation[2]


    def __zero_head(self):
        print("Zeroing head")
        y_difference = -(self.__bed_level - self.nozzle_position[1])
        x_difference = -(self.__plate_x_zero - self.nozzle_position[0])
        z_difference = (self.__plate_z_zero - self.nozzle_position[2])
        max_difference = max(y_difference, x_difference, z_difference)
        print("Bed: %d | Nozzle: %d" % (self.__bed_level, self.nozzle_position[1]))
        print("Edge: %d | Nozzle: %d" % (self.__plate_x_zero, self.nozzle_position[0]))
        print("Plate: %d | Nozzle: %d" % (self.__plate_z_zero, self.nozzle_position[2]))
        for y in range(int(max_difference)):
            self.command_queue.put(
                (
                    -(math.ceil(x_difference / max_difference)),
                    -(math.ceil(y_difference / max_difference)),
                    -(math.ceil(z_difference / max_difference))
                ))
            y_difference -= 1
            x_difference -= 1
            z_difference -= 1


    def __manual_test(self, event):
        match event.key:
            case pygame.K_j:
                self.__model_x_position -= self.__movement_rate
                print("X: %d | Y: %d | Z: %d" % (self.__model_x_position, self.__model_y_position, self.__model_z_position))
            case pygame.K_k:
                self.__model_x_position += self.__movement_rate
                print("X: %d | Y: %d | Z: %d" % (self.__model_x_position, self.__model_y_position, self.__model_z_position))
            case pygame.K_o:
                self.__model_y_position -= self.__movement_rate
                print("X: %d | Y: %d | Z: %d" % (self.__model_x_position, self.__model_y_position, self.__model_z_position))
            case pygame.K_p:
                self.__model_y_position += self.__movement_rate
                print("X: %d | Y: %d | Z: %d" % (self.__model_x_position, self.__model_y_position, self.__model_z_position))
            case pygame.K_n:
                self.__model_z_position -= self.__movement_rate
                print("X: %d | Y: %d | Z: %d" % (self.__model_x_position, self.__model_y_position, self.__model_z_position))
            case pygame.K_m:
                self.__model_z_position += self.__movement_rate
                print("X: %d | Y: %d | Z: %d" % (self.__model_x_position, self.__model_y_position, self.__model_z_position))
            case pygame.K_f:
                self.__zero_head()

    def __reset_printer(self, event):
        if event.key == pygame.K_z:  # resets x and y positions
            self.__model_x_position = 0
            self.__model_y_position = 0
            self.__model_z_position = 0
            print("X: %d | Y: %d | Z: %d" % (self.__model_x_position, self.__model_y_position, self.__model_z_position))

    def update_printer_frame(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self.__build_printer_head()
        self.__build_horizontal_rail()
        self.__build_vertical_rail()
        self.__build_plate()

    def __build_printer_head(self):
        glBegin(GL_LINES)
        head = PrinterHead(self.__dimension, self.__x_offset, self.__model_x_position, self.__model_y_position)
        for part in head.all_parts:
            for edge in part[1]:
                for vertex in edge:
                    glVertex3fv(part[0][vertex])

        glEnd()
        self.nozzle_position = head.get_nozzle_position()

    def __build_horizontal_rail(self):
        glBegin(GL_LINES)
        horizontal_rail = HorizontalRail(self.__dimension, self.__x_offset, self.__model_y_position)
        for part in horizontal_rail.all_parts:
            for edge in part[1]:
                for vertex in edge:
                    glVertex3fv(part[0][vertex])

        glEnd()

    def __build_vertical_rail(self):
        glBegin(GL_LINES)
        vertical_rail = VerticalRail(self.__dimension, self.__x_offset)
        for part in vertical_rail.all_parts:
            for edge in part[1]:
                for vertex in edge:
                    glVertex3fv(part[0][vertex])

        glEnd()

    def __build_plate(self):
        glBegin(GL_LINES)
        plate = Plate(self.__dimension, self.__x_offset, self.__bed_level, self.__model_z_position)
        for part in plate.all_parts:
            for edge in part[1]:
                for vertex in edge:
                    glVertex3fv(part[0][vertex])

        glEnd()
        self.__plate_x_zero = plate.get_x_zero()
        self.__plate_z_zero = plate.get_z_zero()
