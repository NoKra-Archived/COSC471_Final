class Plate:
    def __init__(self, dimension, current_z):
        self.dimension = dimension
        self.current_z = current_z
        self.y_height = dimension * 4.5

        self.plate = self.__create_plate()
        self.sled = self.__create_sled()
        self.all_parts = (self.plate, self.sled)

    def __create_plate(self):
        plate_dimension = self.dimension * 2.4

        front_right = (0, -self.y_height, plate_dimension + self.current_z)
        front_left = (- plate_dimension * 2, - self.y_height, plate_dimension + self.current_z)
        back_right = (0, - self.y_height, - plate_dimension + self.current_z)
        back_left = (- plate_dimension * 2, -self.y_height, - plate_dimension + self.current_z)

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