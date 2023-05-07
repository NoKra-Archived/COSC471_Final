
class VerticalRail:
    def __init__(self, dimension, x_offset):
        self.__dimension = dimension
        self.__x_offset = x_offset
        self.__z_offset = dimension / 2
        self.__x_position = (dimension / 5) + (dimension / 8)
        self.__y_offset = dimension / 2
        self.__rail_base_length = (dimension / 2) / 1.5
        self.__rail_base_length_midpoint = self.__rail_base_length / 2
        self.__rail_base_width = dimension * 0.8
        self.__rail_base_width_midpoint = self.__rail_base_width * 0.5

        self.__cap_width = dimension * 0.5
        self.__cap_height = dimension / 4
        self.__rail_length = dimension * 5
        self.__rail_width = dimension * 0.1

        self.__top_cap = self.__create_top_cap()
        self.__rail_left = self.__create_left_rail()
        self.__rail_right = self.__create_right_rail()
        self.__rail_base = self.__create_rail_base()
        self.all_parts = (self.__top_cap, self.__rail_left, self.__rail_right, self.__rail_base)


    def __create_top_cap(self):
        cap_y_gap = self.__dimension * 0.1

        rail_base_midpoint = (self.__x_position + self.__rail_base_width_midpoint + self.__x_offset, self.__y_offset + cap_y_gap, -self.__z_offset - self.__rail_base_length - self.__rail_base_length_midpoint)
        bottom_front = (rail_base_midpoint[0], rail_base_midpoint[1], rail_base_midpoint[2] + self.__cap_width)
        bottom_left = (rail_base_midpoint[0] - self.__cap_width, rail_base_midpoint[1], rail_base_midpoint[2])
        bottom_right = (rail_base_midpoint[0] + self.__cap_width, rail_base_midpoint[1], rail_base_midpoint[2])
        bottom_back = (rail_base_midpoint[0], rail_base_midpoint[1], rail_base_midpoint[2] - self.__cap_width)
        top_front = (bottom_front[0], bottom_front[1] + self.__cap_height, bottom_front[2])
        top_left = (bottom_left[0], bottom_left[1] + self.__cap_height, bottom_left[2])
        top_right = (bottom_right[0], bottom_right[1] + self.__cap_height, bottom_right[2])
        top_back = (bottom_back[0], bottom_back[1] + self.__cap_height, bottom_back[2])

        vertices = (
            bottom_front,  # 0
            bottom_left,  # 1
            bottom_right,  # 2
            bottom_back,  # 3
            top_front,  # 4
            top_left,  # 5
            top_right,  # 6
            top_back,  # 7
            rail_base_midpoint,  # 8
        )

        edges = (
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 6),
            (5, 7),
            (6, 7)
        )

        return vertices, edges

    def __create_left_rail(self):
        offset_rail = self.__dimension * 0.15

        top_cap_left_bottom = self.__top_cap[0][1]
        top_left = (top_cap_left_bottom[0] + offset_rail, top_cap_left_bottom[1], top_cap_left_bottom[2])
        top_front = (top_left[0] + self.__rail_width, top_left[1], top_left[2] + self.__rail_width)
        top_back = (top_left[0] + self.__rail_width, top_left[1], top_left[2] - self.__rail_width)
        top_right = (top_front[0] + self.__rail_width, top_front[1], top_front[2] - self.__rail_width)
        bottom_left = (top_left[0], top_left[1] - self.__rail_length, top_left[2])
        bottom_front = (top_front[0], top_front[1] - self.__rail_length, top_front[2])
        bottom_back = (top_back[0], top_back[1] - self.__rail_length, top_back[2])
        bottom_right = (top_right[0], top_right[1] - self.__rail_length, top_right[2])
        top_cap_front_bottom = self.__top_cap[0][0]
        top_cap_back_bottom = self.__top_cap[0][3]
        cap_attach_front = (top_cap_front_bottom[0], top_cap_front_bottom[1], top_cap_front_bottom[2] - offset_rail)
        cap_attach_back = (top_cap_back_bottom[0], top_cap_back_bottom[1], top_cap_back_bottom[2] + offset_rail)
        cap_attach_back_center = (cap_attach_back[0], cap_attach_back[1], cap_attach_back[2] + self.__dimension * .2)
        cap_attach_front_center = (cap_attach_front[0], cap_attach_front[1], cap_attach_front[2] - self.__dimension * .2)

        vertices = (
            top_cap_left_bottom,  # 0
            top_left,  # 1
            top_front,  # 2
            top_back,  # 3
            top_right,  # 4
            bottom_left,  # 5
            bottom_front,  # 6
            bottom_back,  # 7
            bottom_right,  # 8
            top_cap_back_bottom,  # 9
            top_cap_front_bottom,  # 10
            cap_attach_back,  # 11
            cap_attach_front,  # 12
            cap_attach_back_center,  # 13
            cap_attach_front_center,  # 14
        )

        edges = (
            (0, 1),
            (1, 2),
            (1, 3),
            (2, 4),
            (3, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 8),
            (9, 11),
            (10, 12),
            (2, 12),
            (3, 11),
            (5, 6),
            (5, 7),
            (6, 8),
            (7, 8),
            (4, 13),
            (4, 14),
            (11, 13),
            (12, 14)
        )

        return vertices, edges

    def __create_right_rail(self):
        offset_rail = self.__dimension * 0.15

        top_cap_right_bottom = self.__top_cap[0][2]
        top_right = (top_cap_right_bottom[0] - offset_rail, top_cap_right_bottom[1], top_cap_right_bottom[2])
        top_front = (top_right[0] - self.__rail_width, top_right[1], top_right[2] + self.__rail_width)
        top_back = (top_right[0] - self.__rail_width, top_right[1], top_right[2] - self.__rail_width)
        top_left = (top_front[0] - self.__rail_width, top_front[1], top_front[2] - self.__rail_width)
        bottom_right = (top_right[0], top_right[1] - self.__rail_length, top_right[2])
        bottom_front = (top_front[0], top_front[1] - self.__rail_length, top_front[2])
        bottom_back = (top_back[0], top_back[1] - self.__rail_length, top_back[2])
        bottom_left = (top_left[0], top_left[1] - self.__rail_length, top_left[2])
        cap_attach_back = self.__rail_left[0][11]
        cap_attach_front = self.__rail_left[0][12]
        cap_attach_back_center = self.__rail_left[0][13]
        cap_attach_front_center = self.__rail_left[0][14]

        vertices = (
            top_cap_right_bottom,  # 0
            top_right,  # 1
            top_front,  # 2
            top_back,  # 3
            top_left,  # 4
            bottom_right,  # 5
            bottom_front,  # 6
            bottom_back,  # 7
            bottom_left,  # 8
            cap_attach_back,  # 9
            cap_attach_front,  # 10
            cap_attach_back_center,  # 11
            cap_attach_front_center,  # 12
        )

        edges = (
            (0, 1),
            (1, 2),
            (1, 3),
            (2, 4),
            (3, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 8),
            (5, 6,),
            (5, 7),
            (8, 6),
            (8, 7),
            (2, 10),
            (3, 9),
            (4, 11),
            (4, 12)

        )

        return vertices, edges

    def __create_rail_base(self):
        base_width = self.__dimension * 0.5
        base_length = self.__dimension
        base_height = self.__dimension * 0.4
        offset_backward = self.__dimension * 0.8

        rail_top_midpoint = self.__top_cap[0][8]
        rail_bottom_midpoint = (rail_top_midpoint[0], rail_top_midpoint[1] - self.__rail_length, rail_top_midpoint[2] - offset_backward)
        top_front_left = (rail_bottom_midpoint[0] - base_width, rail_bottom_midpoint[1], rail_bottom_midpoint[2] + base_length)
        top_front_right = (rail_bottom_midpoint[0] + base_width, rail_bottom_midpoint[1], rail_bottom_midpoint[2] + base_length)
        top_back_left = (rail_bottom_midpoint[0] - base_width, rail_bottom_midpoint[1], rail_bottom_midpoint[2] - base_length)
        top_back_right = (rail_bottom_midpoint[0] + base_width, rail_bottom_midpoint[1], rail_bottom_midpoint[2] - base_length)
        bottom_front_left = (top_front_left[0], top_front_left[1] - base_height, top_front_left[2])
        bottom_front_right = (top_front_right[0], top_front_right[1] - base_height, top_front_right[2])
        bottom_back_left = (top_back_left[0], top_back_left[1] - base_height, top_back_left[2])
        bottom_back_right = (top_back_right[0], top_back_right[1] - base_height, top_back_right[2])

        vertices = (
            top_front_left,  # 0
            top_front_right,  # 1
            top_back_left,  # 2
            top_back_right,  # 3
            bottom_front_left,  # 4
            bottom_front_right,  # 5
            bottom_back_left,  # 6
            bottom_back_right,  # 7

        )

        edges =(
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 6),
            (5, 7),
            (6, 7)

        )

        return vertices, edges
