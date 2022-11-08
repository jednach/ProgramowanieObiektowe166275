class Point(object):
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def print(self):
        print(f'({self.x}, {self.y})')

    @staticmethod
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5


def main():
    pkt1 = Point(1, 2)
    pkt2 = Point(0, 1)
    print(pkt1.distance(pkt1, pkt2))


if __name__ == '__main__':
    main()
