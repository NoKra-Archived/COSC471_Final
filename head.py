
# instead of hard-coding the sizes and connections, using classes to build the printer parts
# probably best to have head_height and head_length be even in size
class PrinterHead:
    def __init__(self, head_width, head_height, head_length):
        self.head_width = head_width
        self.head_height = head_height / 2
        self.head_length = head_length / 2
        self.main_box = self.__create_main_box()
        self.fan_box = self.__create_fan_box()
        self.nozzle = self.__create_nozzle()
        self.carriage_block = self.__create_carriage_block()
        self.all_parts = (self.main_box, self.fan_box, self.nozzle, self.carriage_block)

    def __create_main_box(self):
        vertices = (
            # right bottom back 0
            (self.head_width, -self.head_height, -self.head_length),
            # right top back 1
            (self.head_width, self.head_height, -self.head_length),
            # left top back 2
            (-self.head_width, self.head_height, -self.head_length),
            # left bottom back 3
            (-self.head_width, -self.head_height, -self.head_length),
            # right bottom front 4
            (self.head_width, -self.head_height, self.head_length),
            # right top front 5
            (self.head_width, self.head_height, self.head_length),
            # left bottom front 6
            (-self.head_width, -self.head_height, self.head_length),
            # left top front 7
            (-self.head_width, self.head_height, self.head_length)
        )

        edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
        )
        return vertices, edges

    def __create_fan_box(self):
        offset = self.head_height / 2.5 # Used for constant distance measurements
        # Box attachment points
        box_left_bottom_front = self.main_box[0][6]
        box_left_top_front = self.main_box[0][7]
        box_left_bottom_back = self.main_box[0][3]
        box_left_top_back = self.main_box[0][2]
        # Fan attachment points
        bottom_front_connection = (box_left_bottom_front[0], box_left_bottom_front[1] + offset, box_left_bottom_front[2] - offset)
        top_front_connection = (box_left_top_front[0], box_left_top_front[1] - offset, box_left_top_front[2] - offset)
        bottom_back_connection = (box_left_bottom_back[0], box_left_bottom_back[1] + offset, box_left_bottom_back[2] + offset)
        top_back_connection = (box_left_top_back[0], box_left_top_back[1] - offset, box_left_top_back[2] + offset)
        # Fan body points
        bottom_front_fan = (bottom_front_connection[0] - offset, bottom_front_connection[1], bottom_front_connection[2])
        top_front_fan = (top_front_connection[0] - offset, top_front_connection[1], top_front_connection[2])
        bottom_back_fan = (bottom_back_connection[0] - offset, bottom_back_connection[1], bottom_back_connection[2])
        top_back_fan = (top_back_connection[0] - offset, top_back_connection[1], top_back_connection[2])

        vertices = (
            box_left_bottom_front,  # 0
            box_left_top_front,  # 1
            box_left_bottom_back,  # 2
            box_left_top_back,  # 3
            bottom_front_connection,  # 4
            top_front_connection,  # 5
            bottom_back_connection,  # 6
            top_back_connection,  # 7
            bottom_front_fan,  # 8
            top_front_fan,  # 9
            bottom_back_fan,  # 10
            top_back_fan  # 11
        )

        edges = (
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 6),
            (5, 7),
            (6, 7),
            (4, 8),
            (5, 9),
            (6, 10),
            (7, 11),
            (8, 9),
            (8, 10),
            (9, 11),
            (10, 11)
        )
        return vertices, edges

    def __create_nozzle(self):
        offset = self.head_length / 2.5
        # Box attachment points
        box_left_front = self.main_box[0][6]
        box_right_front = self.main_box[0][4]
        box_left_back = self.main_box[0][3]
        box_right_back = self.main_box[0][0]
        # Stem attachment points
        left_front_attach = (box_left_front[0] / 2, box_left_front[1], box_left_front[2] - offset)
        right_front_attach = (box_right_front[0] / 2, box_right_front[1], box_right_front[2] - offset)
        left_back_attach = (box_left_back[0] / 2, box_left_back[1], left_front_attach[2] - offset)
        right_back_attach = (box_right_back[0] / 2, box_right_back[1], right_front_attach[2] - offset)
        # Stem length points
        left_front_stem = (left_front_attach[0], left_front_attach[1] - (offset / 2), left_front_attach[2])
        right_front_stem = (right_front_attach[0], right_front_attach[1] - (offset / 2), right_front_attach[2])
        left_back_stem = (left_back_attach[0], left_back_attach[1] - (offset / 2), left_back_attach[2])
        right_back_stem = (right_back_attach[0], right_back_attach[1] - (offset / 2), right_back_attach[2])
        # Heat sink top points
        left_front_sink_top = (box_left_front[0], left_front_stem[1], box_left_front[2])
        right_front_sink_top = (box_right_front[0], right_front_stem[1], box_right_front[2])
        left_back_sink_top = (box_left_back[0], left_back_stem[1], left_back_stem[2] - offset)
        right_back_sink_top = (box_right_back[0], right_back_stem[1], right_back_stem[2] - offset)
        # Heat sink bottom points
        left_front_sink_bottom = (left_front_sink_top[0], left_front_sink_top[1] - (offset / 2), left_front_sink_top[2])
        right_front_sink_bottom = (right_front_sink_top[0], right_front_sink_top[1] - (offset / 2), right_front_sink_top[2])
        left_back_sink_bottom = (left_back_sink_top[0], left_back_sink_top[1] - (offset / 2), left_back_sink_top[2])
        right_back_sink_bottom = (right_back_sink_top[0], right_back_sink_top[1] - (offset / 2), right_back_sink_top[2])
        left_mid_sink_bottom = (left_front_sink_bottom[0], left_back_sink_bottom[1] - (offset / 2), left_back_stem[2])
        right_mid_sink_bottom = (right_front_sink_bottom[0], right_back_sink_bottom[1] - (offset / 2), right_back_stem[2])
        # Nozzle attachment points (y coordinates are temporary, may do some linear interpolation)
        left_front_nozzle_top = (left_front_sink_bottom[0] + (offset / 2), left_front_sink_bottom[1] - offset / 3, left_front_sink_bottom[2] - (offset / 2))
        right_front_nozzle_top = (right_front_sink_bottom[0] - (offset / 2), right_front_sink_bottom[1] - offset / 3, right_front_sink_bottom[2] - (offset / 2))
        mid_front_nozzle_top = (0, left_front_sink_bottom[1] - offset / 3, left_front_nozzle_top[2] + (offset / 4))
        mid_front_sink_attach = (0, left_front_sink_bottom[1], left_front_sink_bottom[2])
        left_back_nozzle_top = (left_front_nozzle_top[0], left_front_nozzle_top[1], left_front_nozzle_top[2] - (offset / 2))
        right_back_nozzle_top = (right_front_nozzle_top[0], right_front_nozzle_top[1], right_front_nozzle_top[2] - (offset / 2))
        mid_back_nozzle_top = (0, left_front_nozzle_top[1], left_back_nozzle_top[2] - (offset / 4))
        mid_back_sink_attach = (0, left_mid_sink_bottom[1], left_mid_sink_bottom[2])
        # Nozzle body points
        left_front_nozzle_bottom = (left_front_nozzle_top[0], left_front_nozzle_top[1] - (offset / 2), left_front_nozzle_top[2])
        right_front_nozzle_bottom = (right_front_nozzle_top[0], right_front_nozzle_top[1] - (offset / 2), right_front_nozzle_top[2])
        mid_front_nozzle_bottom = (0, mid_back_nozzle_top[1] - (offset / 2), mid_front_nozzle_top[2])
        left_back_nozzle_bottom = (left_back_nozzle_top[0], left_back_nozzle_top[1] - (offset / 2), left_back_nozzle_top[2])
        right_back_nozzle_bottom = (right_back_nozzle_top[0], right_back_nozzle_top[1] - (offset / 2), right_back_nozzle_top[2])
        mid_back_nozzle_bottom = (0, mid_back_nozzle_top[1] - (offset / 2), mid_back_nozzle_top[2])
        # Nozzle tip points
        left_front_tip_attach = (left_front_nozzle_bottom[0] + (offset / 6), left_front_nozzle_bottom[1], left_front_nozzle_bottom[2] - (offset / 6))
        right_front_tip_attach = (right_front_nozzle_bottom[0] - (offset / 6), right_front_nozzle_bottom[1], right_front_nozzle_bottom[2] - (offset / 6))
        mid_front_tip_attach = (0, mid_front_nozzle_bottom[1], mid_front_nozzle_bottom[2] - (offset / 6))
        left_back_tip_attach = (left_back_nozzle_bottom[0] + (offset / 6), left_back_nozzle_bottom[1], left_back_nozzle_bottom[2] + (offset / 6))
        right_back_tip_attach = (right_back_nozzle_bottom[0] - (offset / 6), right_back_nozzle_bottom[1], right_back_nozzle_bottom[2] + (offset / 6))
        mid_back_tip_attach = (0, mid_back_nozzle_bottom[1], mid_back_nozzle_bottom[2] + (offset / 6))
        nozzle_tip = (0, mid_front_tip_attach[1] - (offset / 3), left_front_nozzle_bottom[2] - (offset / 4))

        vertices = (
            box_left_front,  # 0
            box_right_front,  # 1
            box_left_back,  # 2
            box_right_back,  # 3
            left_front_attach,  # 4
            right_front_attach,  # 5
            left_back_attach,  # 6
            right_back_attach,  # 7
            left_front_stem,  # 8
            right_front_stem,  # 9
            left_back_stem,  # 10
            right_back_stem,  # 11
            left_front_sink_top,  # 12
            right_front_sink_top,  # 13
            left_back_sink_top,  # 14
            right_back_sink_top,  # 15
            left_front_sink_bottom,  # 16
            right_front_sink_bottom,  # 17
            left_back_sink_bottom,  # 18
            right_back_sink_bottom,  # 19
            left_mid_sink_bottom,  # 20
            right_mid_sink_bottom,  # 21
            left_front_nozzle_top,  # 22
            right_front_nozzle_top,  # 23
            mid_front_nozzle_top,  # 24
            mid_front_sink_attach,  # 25
            left_back_nozzle_top,  # 26
            right_back_nozzle_top,  # 27
            mid_back_nozzle_top,  # 28
            mid_back_sink_attach,  # 29
            left_front_nozzle_bottom,  # 30
            right_front_nozzle_bottom,  # 31
            mid_front_nozzle_bottom,  # 32
            left_back_nozzle_bottom,  # 33
            right_back_nozzle_bottom,  # 34
            mid_back_nozzle_bottom,  # 35
            left_front_tip_attach,  # 36
            right_front_tip_attach,  # 37
            mid_front_tip_attach,  # 38
            left_back_tip_attach,  # 39
            right_back_tip_attach,  # 40
            mid_back_tip_attach,  # 41
            nozzle_tip,  # 42
        )

        edges = (
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 6),
            (5, 7),
            (6, 7),
            (4, 8),
            (5, 9),
            (6, 10),
            (7, 11),
            (8, 9),
            (8, 10),
            (9, 11),
            (10, 11),
            (8, 12),
            (9, 13),
            (10, 14),
            (11, 15),
            (12, 13),
            (12, 14),
            (13, 15),
            (14, 15),
            (12, 16),
            (13, 17),
            (14, 18),
            (15, 19),
            (16, 17),
            (18, 19),
            (16, 20),
            (18, 20),
            (17, 21),
            (19, 21),
            (20, 21),
            (16, 22),
            (17, 23),
            (22, 24),
            (23, 24),
            (24, 25),
            (20, 26),
            (22, 26),
            (21, 27),
            (23, 27),
            (26, 28),
            (27, 28),
            (28, 29),
            (22, 30),
            (23, 31),
            (24, 32),
            (26, 33),
            (27, 34),
            (28, 35),
            (30, 32),
            (31, 32),
            (30, 33),
            (31, 34),
            (33, 35),
            (34, 35),
            (30, 36),
            (31, 37),
            (32, 38),
            (33, 39),
            (34, 40),
            (35, 41),
            (36, 38),
            (37, 38),
            (36, 39),
            (37, 40),
            (39, 41),
            (40, 41),
            (36, 42),
            (37, 42),
            (38, 42),
            (39, 42),
            (40, 42),
            (41, 42)

        )
        return vertices, edges


    def __create_carriage_block(self):
        offset = self.head_length / 1.5
        # Box attachment points
        box_left_top_back = self.main_box[0][2]
        box_right_top_back = self.main_box[0][1]
        box_left_bottom_back = self.main_box[0][3]
        box_right_bottom_back = self.main_box[0][0]
        # Carriage body
        body_left_top = (box_left_top_back[0], box_left_top_back[1], box_left_top_back[2] - offset)
        body_mid_left_top_anchor = (box_left_top_back[0], box_left_top_back[1], box_left_top_back[2] - offset / 2)
        body_right_top = (box_right_top_back[0], box_right_top_back[1], box_right_top_back[2] - offset)
        body_mid_right_top_anchor = (box_right_top_back[0], box_right_top_back[1], box_right_top_back[2] - offset / 2)
        body_left_bottom = (box_left_bottom_back[0], box_left_bottom_back[1], box_left_bottom_back[2] - offset)
        body_mid_left_bottom_anchor = (box_left_bottom_back[0], box_left_bottom_back[1], box_left_bottom_back[2] - offset / 2)
        body_right_bottom = (box_right_bottom_back[0], box_right_bottom_back[1], box_right_bottom_back[2] - offset)
        body_mid_right_bottom_anchor = (box_right_bottom_back[0], box_right_bottom_back[1], box_right_bottom_back[2] - offset / 2)
        # figure out the mid-point, probably height / 2 of the main box or something
        body_left_mid_top_anchor = (body_left_top[0], body_left_top[1], body_left_top[2])
        body_left_mid_bottom_anchor = (body_left_bottom[0], body_left_bottom[1], body_left_bottom[2])
        body_right_mid_top_anchor = (body_right_top[0], body_right_top[1], body_right_top[2])
        body_right_mid_bottom_anchor = (body_right_bottom[0], body_right_bottom[1], body_right_bottom[2])
        # Guide rod bearing top (abbr. tbl = top bearing left, bbl = bottom bearing left, etc.)
        tbl_mid_top_attach = (body_left_top[0], body_left_top[1] - offset / 3, body_left_top[2] + (offset / 2))
        tbl_left_top_attach = (tbl_mid_top_attach[0], tbl_mid_top_attach[1] - offset / 2, tbl_mid_top_attach[2] - offset / 2)


        vertices = (
            box_left_top_back,  # 0
            box_right_top_back,  # 1
            box_left_bottom_back,  # 2
            box_right_bottom_back,  # 3
            body_left_top,  # 4
            body_right_top,  # 5
            body_left_bottom,  # 6
            body_right_bottom,  # 7
            body_mid_left_top_anchor,  # 8,
            body_mid_right_top_anchor,  # 9
            body_mid_left_bottom_anchor,  # 10
            body_mid_right_bottom_anchor,  # 11
            body_left_mid_top_anchor,  # 12
            body_left_mid_bottom_anchor,  # 13
            body_right_mid_top_anchor,  # 14
            body_right_mid_bottom_anchor,  # 15
            tbl_mid_top_attach,  # 16
            tbl_left_top_attach,  # 17
        )

        edges = (
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 6),
            (5, 7),
            (6, 7),
            (8, 16),
            (16, 17)

        )

        return vertices, edges
