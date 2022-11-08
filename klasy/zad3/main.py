import math


class SodaCan(object):

    def __init__(self, init_x, init_y):
        self.h = init_x
        self.r = init_y

    def get_surface_area(self):
        return 2 * math.pi * self.r ** 2 + 2 * math.pi * self.r * self.h

    def get_volume(self):
        return math.pi * self.r ** 2 * self.h


def main():
    can = SodaCan(1, 2)
    print(can.get_surface_area())
    print(can.get_volume())


if __name__ == '__main__':
    main()
