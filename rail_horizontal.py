
class HorizontalRail:
    def __init__(self, dimension, current_y):
        self.dimension = dimension
        self.current_y = current_y
        self.z_offset = dimension / 2
        self.x_offset = (dimension / 5) + (dimension / 8) # dimension / 8 is the gap size between the base
        self.base_length = (dimension / 2) / 1.5
        self.base_width = dimension * 0.8
        self.base_height = dimension / 2

        self.horizontal_rail_base = self.__create_horizontal_rail_base()
        self.vertical_rail_base = self.__create_vertical_rail_base()
        self.horizontal_rail = self.__create_horizontal_rail()
        self.all_parts = (self.horizontal_rail_base, self.vertical_rail_base, self.horizontal_rail)

    def __create_horizontal_rail_base(self):
        left_bottom_back = (self.x_offset, -self.base_height + self.current_y, -self.z_offset - self.base_length)
        right_bottom_back = (self.x_offset + self.base_width, -self.base_height + self.current_y, -self.z_offset - self.base_length)
        left_bottom_front = (self.x_offset, - self.base_height + self.current_y, -self.z_offset)
        right_bottom_front = (self.x_offset + self.base_width, - self.base_height + self.current_y, -self.z_offset)
        left_top_back = (self.x_offset, self.base_height + self.current_y, -self.z_offset - self.base_length)
        right_top_back = (self.x_offset + self.base_width, self.base_height + self.current_y, -self.z_offset - self.base_length)
        left_top_front = (self.x_offset, self.base_height + self.current_y, -self.z_offset)
        right_top_front = (self.x_offset + self.base_width, self.base_height + self.current_y, -self.z_offset)

        vertices = (
            left_bottom_back,  # 0
            right_bottom_back,  # 1
            left_bottom_front,  # 2
            right_bottom_front,  # 3
            left_top_back,  # 4
            right_top_back,  # 5
            left_top_front,  # 6
            right_top_front,  # 7
        )

        edges = (
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3),
            (0, 4),
            (1, 5),
            (4, 5),
            (4, 6),
            (2, 6),
            (6, 7),
            (3, 7),
            (5, 7)
        )

        return vertices, edges

    def __create_vertical_rail_base(self):
        left_bottom_front = self.horizontal_rail_base[0][0]
        right_bottom_front = self.horizontal_rail_base[0][1]
        left_top_front = self.horizontal_rail_base[0][4]
        right_top_front = self.horizontal_rail_base[0][5]
        left_bottom_back = (left_bottom_front[0], left_bottom_front[1], left_bottom_front[2] - self.base_length)
        right_bottom_back = (right_bottom_front[0], right_bottom_front[1], right_bottom_front[2] - self.base_length)
        left_top_back = (left_top_front[0], left_top_front[1], left_top_front[2] - self.base_length)
        right_top_back = (right_top_front[0], right_top_front[1], right_top_front[2] - self.base_length)

        vertices = (
            left_bottom_front,  # 0
            right_bottom_front,  # 1
            left_top_front,  # 2
            right_top_front,  # 3
            left_bottom_back,  # 4
            right_bottom_back,  # 5
            left_top_back,  # 6
            right_top_back,  # 7
        )

        edges = (
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 5),
            (6, 7),
            (4, 6),
            (5, 7)
        )

        return vertices, edges

    def __create_horizontal_rail(self):
        rail_offset = self.dimension * 0.1
        rail_length = self.dimension * 5
        cap_width = self.dimension * 0.4
        base_left_bottom_back = self.horizontal_rail_base[0][0]
        base_left_bottom_front = self.horizontal_rail_base[0][2]
        base_left_top_back = self.horizontal_rail_base[0][4]
        base_left_top_front = self.horizontal_rail_base[0][6]
        # top rail attach
        top_attach_top_back = (base_left_top_back[0], base_left_top_back[1] - rail_offset, base_left_top_back[2] + rail_offset)
        top_attach_top_front = (base_left_top_front[0], base_left_top_front[1] - rail_offset, base_left_top_front[2] - rail_offset)
        base_top_back_attach = (base_left_top_back[0], base_left_top_back[1] - (rail_offset * 3.5), base_left_top_back[2])
        top_attach_bottom_back = (base_top_back_attach[0], base_top_back_attach[1] + rail_offset, base_top_back_attach[2] + rail_offset)
        base_top_front_attach = (base_left_top_front[0], base_left_top_front[1] - (rail_offset * 3.5), base_left_top_front[2])
        top_attach_bottom_front = (base_top_front_attach[0], base_top_front_attach[1] + rail_offset, base_top_front_attach[2] - rail_offset)
        # top rail body
        top_end_top_back = (top_attach_top_back[0] - rail_length, top_attach_top_back[1], top_attach_top_back[2])
        top_end_top_front = (top_attach_top_front[0] - rail_length, top_attach_top_front[1], top_attach_top_front[2])
        top_end_bottom_back = (top_attach_bottom_back[0] - rail_length, top_attach_bottom_back[1], top_attach_bottom_back[2])
        top_end_bottom_front = (top_attach_bottom_front[0] - rail_length, top_attach_bottom_front[1], top_attach_bottom_front[2])
        # bottom rail attach
        base_bottom_back_attach = (base_left_bottom_back[0], base_left_bottom_back[1] + (rail_offset * 3.5), base_left_bottom_back[2])
        base_bottom_front_attach = (base_left_bottom_front[0], base_left_bottom_front[1] + (rail_offset * 3.5), base_left_bottom_front[2])
        bottom_attach_bottom_back = (base_left_bottom_back[0], base_left_bottom_back[1] + rail_offset, base_left_bottom_back[2] + rail_offset)
        bottom_attach_bottom_front = (base_left_bottom_front[0], base_left_bottom_front[1] + rail_offset, base_left_bottom_front[2] - rail_offset)
        bottom_attach_top_back = (base_bottom_back_attach[0], base_bottom_back_attach[1] - rail_offset, base_bottom_back_attach[2] + rail_offset)
        bottom_attach_top_front = (base_bottom_front_attach[0], base_bottom_front_attach[1] - rail_offset, base_bottom_front_attach[2] - rail_offset)
        # bottom rail body
        bottom_end_top_back = (bottom_attach_top_back[0] - rail_length, bottom_attach_top_back[1], bottom_attach_top_back[2])
        bottom_end_top_front = (bottom_attach_top_front[0] - rail_length, bottom_attach_top_front[1], bottom_attach_top_front[2])
        bottom_end_bottom_back = (bottom_attach_bottom_back[0] - rail_length, bottom_attach_bottom_back[1], bottom_attach_bottom_back[2])
        bottom_end_bottom_front = (bottom_attach_bottom_front[0] - rail_length, bottom_attach_bottom_front[1], bottom_attach_bottom_front[2])
        # rail cap attach
        cap_right_top_back = (base_left_top_back[0] - rail_length, base_left_top_back[1], base_left_top_back[2])
        cap_right_top_front = (base_left_top_front[0] - rail_length, base_left_top_front[1], base_left_top_front[2])
        cap_right_bottom_back = (base_left_bottom_back[0] - rail_length, base_left_bottom_back[1], base_left_bottom_back[2])
        cap_right_bottom_front = (base_left_bottom_front[0] - rail_length, base_left_bottom_front[1], base_left_bottom_front[2])
        cap_attach_top_back = (cap_right_top_back[0], cap_right_top_back[1] - (rail_offset * 3.5), cap_right_top_back[2])
        cap_attach_top_front = (cap_right_top_front[0], cap_right_top_front[1] - (rail_offset * 3.5), cap_right_top_front[2])
        cap_attach_bottom_back = (cap_right_bottom_back[0], cap_right_bottom_back[1] + (rail_offset * 3.5), cap_right_bottom_back[2])
        cap_attach_bottom_front = (cap_right_bottom_front[0], cap_right_bottom_front[1] + (rail_offset * 3.5), cap_right_bottom_front[2])
        # rail cap body
        cap_left_top_back = (cap_right_top_back[0] - cap_width, cap_right_top_back[1], cap_right_top_back[2])
        cap_left_top_front = (cap_right_top_front[0] - cap_width, cap_right_top_front[1], cap_right_top_front[2])
        cap_left_bottom_back = (cap_right_bottom_back[0] - cap_width, cap_right_bottom_back[1], cap_right_bottom_back[2])
        cap_left_bottom_front = (cap_right_bottom_front[0] - cap_width, cap_right_bottom_front[1], cap_right_bottom_front[2])


        vertices = (
            base_left_bottom_back,  # 0
            base_left_bottom_front,  # 1
            base_left_top_back,  # 2
            base_left_top_front,  # 3
            top_attach_top_back,  # 4
            top_attach_top_front,  # 5
            base_top_back_attach,  # 6 offset from base corner to give rail width, aligned with base edge
            top_attach_bottom_back,  # 7
            base_top_front_attach,  # 8 offset from base corner to give rail width, aligned with base edge
            top_attach_bottom_front,  # 9
            top_end_top_back,  # 10
            top_end_top_front,  # 11
            top_end_bottom_back,  # 12
            top_end_bottom_front,  # 13
            base_bottom_back_attach,  # 14 offset from base corner to give rail width, aligned with base edge
            base_bottom_front_attach,  # 15 offset from base corner to give rail width, aligned with base edge
            bottom_attach_bottom_back,  # 16
            bottom_attach_bottom_front,  # 17
            bottom_attach_top_back,  # 18
            bottom_attach_top_front,  # 19
            bottom_end_top_back,  # 20
            bottom_end_top_front,  # 21
            bottom_end_bottom_back,  # 22
            bottom_end_bottom_front,  # 23
            cap_right_top_back,  # 24
            cap_right_top_front,  # 25
            cap_right_bottom_back,  # 26
            cap_right_bottom_front,  # 27
            cap_attach_top_back,  # 28
            cap_attach_top_front,  # 29
            cap_attach_bottom_back,  # 30,
            cap_attach_bottom_front,  # 31
            cap_left_top_back,  # 32
            cap_left_top_front,  # 33
            cap_left_bottom_back,  # 34
            cap_left_bottom_front,  # 35
        )

        edges = (
            (2, 4),
            (3, 5),
            (4, 5),
            (6, 7),
            (4, 7),
            (8, 9),
            (7, 9),
            (5, 9),
            (6, 8),
            (4, 10),
            (5,11),
            (7, 12),
            (9, 13),
            (10, 11),
            (12, 13),
            (10, 12),
            (11, 13),
            (0, 16),
            (1, 17),
            (16, 17),
            (14, 18),
            (15, 19),
            (18, 19),
            (16, 18),
            (17, 19),
            (14, 15),
            (18, 20),
            (19, 21),
            (16, 22),
            (17, 23),
            (20, 21),
            (22, 23),
            (20, 22),
            (21, 23),
            (24, 25),
            (26, 27),
            (24, 26),
            (25, 27),
            (10, 24),
            (11, 25),
            (12, 28),
            (13, 29),
            (28, 29),
            (20, 30),
            (21, 31),
            (30, 31),
            (22, 26),
            (23, 27),
            (24, 32),
            (25, 33),
            (26, 34),
            (27, 35),
            (32, 33),
            (34, 35),
            (32, 34),
            (33, 35)
        )

        return vertices, edges