class Plate:
    def __init__(self, dimension, x_offset, bed_level, current_z):
        self.__dimension = dimension
        self.__x_offset = x_offset
        self.__current_z = current_z
        self.__bed_level = bed_level

        self.__plate = self.__create_plate()
        self.__sled = self.__create_sled()
        self.all_parts = (self.__plate, self.__sled)

    def get_x_zero(self):
        return self.__plate[0][1][0]

    def get_z_zero(self):
        return self.__plate[0][1][2]

    def __create_plate(self):
        plate_dimension = self.__dimension * 2.4

        front_right = (0 + self.__x_offset, self.__bed_level, plate_dimension + self.__current_z)
        front_left = (- plate_dimension * 2 + self.__x_offset, self.__bed_level, plate_dimension + self.__current_z)
        back_right = (0 + self.__x_offset, self.__bed_level, - plate_dimension + self.__current_z)
        back_left = (- plate_dimension * 2 + self.__x_offset, self.__bed_level, - plate_dimension + self.__current_z)

        vertices = (
            front_right,  # 0
            front_left,  # 1
            back_right,  # 2
            back_left,  # 3

        )

        edges = (
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3)

        )

        return vertices, edges

    def __create_sled(self):

        vertices = ()

        edges = ()

        return vertices, edges