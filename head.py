
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
        self.all_parts = (self.main_box, self.fan_box, self.nozzle)

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
        fan_offset = self.head_height / 2.5
        # Box attachment points
        box_left_bottom_front = self.main_box[0][6]
        box_left_top_front = self.main_box[0][7]
        box_left_bottom_back = self.main_box[0][3]
        box_left_top_back = self.main_box[0][2]
        # Fan attachment points
        bottom_front_connection = (box_left_bottom_front[0], box_left_bottom_front[1] + fan_offset, box_left_bottom_front[2] - fan_offset)
        top_front_connection = (box_left_top_front[0], box_left_top_front[1] - fan_offset, box_left_top_front[2] - fan_offset)
        bottom_back_connection = (box_left_bottom_back[0], box_left_bottom_back[1] + fan_offset, box_left_bottom_back[2] + fan_offset)
        top_back_connection = (box_left_top_back[0], box_left_top_back[1] - fan_offset, box_left_top_back[2] + fan_offset)
        # Fan body points
        bottom_front_fan = (bottom_front_connection[0] - fan_offset, bottom_front_connection[1], bottom_front_connection[2])
        top_front_fan = (top_front_connection[0] - fan_offset, top_front_connection[1], top_front_connection[2])
        bottom_back_fan = (bottom_back_connection[0] - fan_offset, bottom_back_connection[1], bottom_back_connection[2])
        top_back_fan = (top_back_connection[0] - fan_offset, top_back_connection[1], top_back_connection[2])

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
        attach_offset = self.head_length / 2.5
        # Box attachment points
        box_left_front = self.main_box[0][6]
        box_right_front = self.main_box[0][4]
        box_left_back = self.main_box[0][3]
        box_right_back = self.main_box[0][0]
        # Stem attachment points
        left_front_attach = (box_left_front[0] / 2, box_left_front[1], box_left_front[2] - attach_offset)
        right_front_attach = (box_right_front[0] / 2, box_right_front[1], box_right_front[2] - attach_offset)
        left_back_attach = (box_left_back[0] / 2, box_left_back[1], left_front_attach[2] - attach_offset)
        right_back_attach = (box_right_back[0] / 2, box_right_back[1], right_front_attach[2] - attach_offset)
        # Stem length points
        left_front_stem = (left_front_attach[0], left_front_attach[1] - (attach_offset / 2), left_front_attach[2])
        right_front_stem = (right_front_attach[0], right_front_attach[1] - (attach_offset / 2), right_front_attach[2])
        left_back_stem = (left_back_attach[0], left_back_attach[1] - (attach_offset / 2), left_back_attach[2])
        right_back_stem = (right_back_attach[0], right_back_attach[1] - (attach_offset / 2), right_back_attach[2])
        # Heat sink top points
        left_front_sink_top = (box_left_front[0], left_front_stem[1], box_left_front[2])
        right_front_sink_top = (box_right_front[0], right_front_stem[1], box_right_front[2])
        left_back_sink_top = (box_left_back[0], left_back_stem[1], left_back_stem[2] - attach_offset)
        right_back_sink_top = (box_right_back[0], right_back_stem[1], right_back_stem[2] - attach_offset)
        # Heat sink bottom points
        left_front_sink_bottom = (left_front_sink_top[0], left_front_sink_top[1] - (attach_offset / 2), left_front_sink_top[2])
        right_front_sink_bottom = (right_front_sink_top[0], right_front_sink_top[1] - (attach_offset / 2), right_front_sink_top[2])
        left_back_sink_bottom = (left_back_sink_top[0], left_back_sink_top[1] - (attach_offset / 2), left_back_sink_top[2])
        right_back_sink_bottom = (right_back_sink_top[0], right_back_sink_top[1] - (attach_offset / 2), right_back_sink_top[2])
        left_mid_sink_bottom = (left_front_sink_bottom[0], left_back_sink_bottom[1] - (attach_offset / 2), left_back_stem[2])
        right_mid_sink_bottom = (right_front_sink_bottom[0], right_back_sink_bottom[1] - (attach_offset / 2), right_back_stem[2])
        # Nozzle attachment points (y coordinates are temporary, may do some linear interpolation)
        left_front_nozzle_top = (left_front_sink_bottom[0] + (attach_offset / 2), left_front_sink_bottom[1] - attach_offset / 3, left_front_sink_bottom[2] - (attach_offset / 2))
        right_front_nozzle_top = (right_front_sink_bottom[0] - (attach_offset / 2), right_front_sink_bottom[1] - attach_offset / 3, right_front_sink_bottom[2] - (attach_offset / 2))
        mid_front_nozzle_top = (0, left_front_sink_bottom[1] - attach_offset / 3, left_front_nozzle_top[2] + (attach_offset / 4))
        mid_front_sink_attach = (0, left_front_sink_bottom[1], left_front_sink_bottom[2])
        left_back_nozzle_top = (left_front_nozzle_top[0], left_front_nozzle_top[1], left_front_nozzle_top[2] - (attach_offset / 2))
        right_back_nozzle_top = (right_front_nozzle_top[0], right_front_nozzle_top[1], right_front_nozzle_top[2] - (attach_offset / 2))
        mid_back_nozzle_top = (0, left_front_nozzle_top[1], left_back_nozzle_top[2] - (attach_offset / 4))
        mid_back_sink_attach = (0, left_mid_sink_bottom[1], left_mid_sink_bottom[2])

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
            (28, 29)

        )
        return vertices, edges


