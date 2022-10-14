# zad2
def product(a, b):
    if (len(a[0]) != len(b)):
        print("operacja nie jest możliwa")
        return
    c = [[0] * len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c


def main():
    m1 = [[-1], [3], [4]]
    m2 = [[1, 0, 3]]
    print(product(m1, m2))


if __name__ == '__main__':
    main()
