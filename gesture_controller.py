import math


class GestureController:

    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    @staticmethod
    def is_left_click(distance):
        return distance < 20

    @staticmethod
    def is_right_click(distance):
        return distance < 20

    @staticmethod
    def is_scroll(distance):
        return distance < 20