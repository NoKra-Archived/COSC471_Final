
class VerticalRail:
    def __init__(self, dimension):
        self.dimension = dimension
        self.z_offset = dimension / 2
        self.x_offset = (dimension / 5) + (dimension / 8)
        self.y_offset = dimension / 2
        self.rail_base_length = (dimension / 2) / 1.5
        self.rail_base_length_midpoint = self.rail_base_length / 2
        self.rail_base_width = dimension * 0.8
        self.rail_base_width_midpoint = self.rail_base_width * 0.5

        self.cap_width = dimension * 0.5
        self.cap_height = dimension / 4
        self.rail_length = dimension * 5
        self.rail_width = dimension * 0.1


        self.top_cap = self.__create_top_cap()
        self.rail_left = self.__create_left_rail()
        self.rail_right = self.__create_right_rail()
        self.rail_base = self.__create_rail_base()
        self.all_parts = (self.top_cap, self.rail_left, self.rail_right, self.rail_base)


    def __create_top_cap(self):
        cap_y_gap = self.dimension * 0.1

        rail_base_midpoint = (self.x_offset + self.rail_base_width_midpoint, self.y_offset + cap_y_gap, -self.z_offset - self.rail_base_length - self.rail_base_length_midpoint)
        bottom_front = (rail_base_midpoint[0], rail_base_midpoint[1], rail_base_midpoint[2] + self.cap_width)
        bottom_left = (rail_base_midpoint[0] - self.cap_width, rail_base_midpoint[1], rail_base_midpoint[2])
        bottom_right = (rail_base_midpoint[0] + self.cap_width, rail_base_midpoint[1], rail_base_midpoint[2])
        bottom_back = (rail_base_midpoint[0], rail_base_midpoint[1], rail_base_midpoint[2] - self.cap_width)
        top_front = (bottom_front[0], bottom_front[1] + self.cap_height, bottom_front[2])
        top_left = (bottom_left[0], bottom_left[1] + self.cap_height, bottom_left[2])
        top_right = (bottom_right[0], bottom_right[1] + self.cap_height, bottom_right[2])
        top_back = (bottom_back[0], bottom_back[1] + self.cap_height, bottom_back[2])

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
        offset_rail = self.dimension * 0.15

        top_cap_left_bottom = self.top_cap[0][1]
        top_left = (top_cap_left_bottom[0] + offset_rail, top_cap_left_bottom[1], top_cap_left_bottom[2])
        top_front = (top_left[0] + self.rail_width, top_left[1], top_left[2] + self.rail_width)
        top_back = (top_left[0] + self.rail_width, top_left[1], top_left[2] - self.rail_width)
        top_right = (top_front[0] + self.rail_width, top_front[1], top_front[2] - self.rail_width)
        bottom_left = (top_left[0], top_left[1] - self.rail_length, top_left[2])
        bottom_front = (top_front[0], top_front[1] - self.rail_length, top_front[2])
        bottom_back = (top_back[0], top_back[1] - self.rail_length, top_back[2])
        bottom_right = (top_right[0], top_right[1] - self.rail_length, top_right[2])
        top_cap_front_bottom = self.top_cap[0][0]
        top_cap_back_bottom = self.top_cap[0][3]
        cap_attach_front = (top_cap_front_bottom[0], top_cap_front_bottom[1], top_cap_front_bottom[2] - offset_rail)
        cap_attach_back = (top_cap_back_bottom[0], top_cap_back_bottom[1], top_cap_back_bottom[2] + offset_rail)
        cap_attach_back_center = (cap_attach_back[0], cap_attach_back[1], cap_attach_back[2] + self.dimension * .2)
        cap_attach_front_center = (cap_attach_front[0], cap_attach_front[1], cap_attach_front[2] - self.dimension * .2)

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
        offset_rail = self.dimension * 0.15

        top_cap_right_bottom = self.top_cap[0][2]
        top_right = (top_cap_right_bottom[0] - offset_rail, top_cap_right_bottom[1], top_cap_right_bottom[2])
        top_front = (top_right[0] - self.rail_width, top_right[1], top_right[2] + self.rail_width)
        top_back = (top_right[0] - self.rail_width, top_right[1], top_right[2] - self.rail_width)
        top_left = (top_front[0] - self.rail_width, top_front[1], top_front[2] - self.rail_width)
        bottom_right = (top_right[0], top_right[1] - self.rail_length, top_right[2])
        bottom_front = (top_front[0], top_front[1] - self.rail_length, top_front[2])
        bottom_back = (top_back[0], top_back[1] - self.rail_length, top_back[2])
        bottom_left = (top_left[0], top_left[1] - self.rail_length, top_left[2])
        cap_attach_back = self.rail_left[0][11]
        cap_attach_front = self.rail_left[0][12]
        cap_attach_back_center = self.rail_left[0][13]
        cap_attach_front_center = self.rail_left[0][14]

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
        base_width = self.dimension * 0.5
        base_length = self.dimension
        base_height = self.dimension * 0.4
        offset_backward = self.dimension * 0.8

        rail_top_midpoint = self.top_cap[0][8]
        rail_bottom_midpoint = (rail_top_midpoint[0], rail_top_midpoint[1] - self.rail_length, rail_top_midpoint[2] - offset_backward)
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
