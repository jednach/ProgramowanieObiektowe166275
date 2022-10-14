# zad3

def mult(a, x):
    c = [[0] * len(a[0]) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j] = x * a[i][j]
    return c


def main():
    m1 = [[-1], [2]]
    print(mult(m1, 3))


if __name__ == '__main__':
    main()
