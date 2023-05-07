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

    def __init__(self, tick_rate):
        self.tick_rate = tick_rate
        self.__dimension = 75  # 75 dimension should create the 180mm print plate size (1 to 1)
        self.__bed_level = -self.__dimension * 4.5
        self.__plate_x_zero = 0
        self.__plate_z_zero = 0
        self.__x_offset = self.__dimension * 2.66  # handles the x shift for the entire printer in relation to the camera

        self.__model_x_position = 0
        self.__model_y_position = 0  # model positions account for the 3D model of the printer
        self.__model_z_position = 0
        # The 3D model of the printer shouldn't be used as the position for the g-code instructions
        self.__nozzle_x_position = 0
        self.__nozzle_y_position = 0  # print positions account for position in 3D space of the printer head
        self.__nozzle_z_position = 0

        self.__movement_rate = 0

        self.movement_queue = Queue(maxsize= 0)
        self.nozzle_position = (0, 0, 0)  # updated whenever the head is built

    def get_z_position(self):
        return self.__model_z_position

    def get_nozzle_position(self):
        # print("Actual Nozzle - X: %d | Y: %d | Z: %d" % (self.nozzle_position[0], self.nozzle_position[1], self.nozzle_position[2]))
        # print("Assumed Position - X: %d | Y: %d | Z: %d" % (self.__nozzle_x_position, self.__nozzle_y_position, self.__nozzle_z_position))
        # print("Model Position - X: %d | Y: %d | Z: %d" % (self.__model_x_position, self.__model_y_position, self.__model_z_position))
        return self.nozzle_position[0],  self.nozzle_position[1], (self.__model_z_position - self.nozzle_position[2])

    def start_print(self, g_code):
        self.__zero_head()

        g_code.populate_command_queue()

    def update_printer_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.__reset_printer(event)

    def move_printer(self):
        movement_info = self.movement_queue.get()
        self.__model_x_position += movement_info[0]
        self.__model_y_position += movement_info[1]
        self.__model_z_position += movement_info[2]

        self.__nozzle_x_position += movement_info[0]
        self.__nozzle_y_position += movement_info[2]
        self.__nozzle_z_position += movement_info[1]

        return movement_info[3]  # returns whether a point should be extruded

    def g_code_plane_movement(self, coordinate_info):
        x_difference = abs(float(coordinate_info[0]) - self.__nozzle_x_position)
        y_difference = abs(float(coordinate_info[1]) - self.__nozzle_y_position)
        line_length = math.sqrt((x_difference ** 2) + (y_difference ** 2))  # length in mm of movement line
        required_ticks = max(int(line_length / self.__movement_rate), 1)
        x_step = (x_difference / required_ticks) if self.__nozzle_x_position < float(coordinate_info[0]) \
            else -(x_difference / required_ticks)
        y_step = (y_difference / required_ticks) if self.__nozzle_y_position < float(coordinate_info[1]) \
            else -(y_difference / required_ticks)

        for tick in range(required_ticks):
            self.movement_queue.put((x_step, 0, y_step, coordinate_info[2]))  # print plane has z and y flipped with 3D view plane

    def g_code_layer_movement(self, target_height):
        z_difference = abs(float(target_height) - self.__nozzle_z_position)
        required_ticks = max(int(z_difference / self.__movement_rate), 1)
        z_step = (z_difference / required_ticks) if self.__nozzle_z_position < float(target_height) \
            else -(z_difference / required_ticks)
        for tick in range(required_ticks):
            self.movement_queue.put((0, z_step, 0, False))
        print("Z height change: %s" % target_height)

    def __zero_head(self):
        print("Zeroing head")
        x_difference = -(self.__plate_x_zero - self.nozzle_position[0])
        y_difference = -(self.__bed_level - self.nozzle_position[1])
        z_difference = (self.__plate_z_zero - self.nozzle_position[2])
        self.__nozzle_x_position = x_difference
        self.__nozzle_y_position = z_difference
        self.__nozzle_z_position = y_difference
        max_difference = max(y_difference, x_difference, z_difference)
        for y in range(int(max_difference)):
            self.movement_queue.put(
                (
                    -(math.ceil(x_difference / max_difference)),
                    -(math.ceil(y_difference / max_difference)),
                    -(math.ceil(z_difference / max_difference)),
                    False
                ))
            y_difference -= 1
            x_difference -= 1
            z_difference -= 1

    def adjust_feed_rate(self, feed_rate):
        mm_per_ms = int(feed_rate) / 60000.0
        self.__movement_rate = mm_per_ms * self.tick_rate
        print("New movement rate: %f" % self.__movement_rate)

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
        glColor3d(1.0, 1.0, 1.0)
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
