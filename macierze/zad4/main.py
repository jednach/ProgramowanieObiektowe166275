# zad4

def tranps(a):
    c = [[0] * len(a) for i in range(len(a[0]))]
    for i in range(len(a[0])):
        for j in range(len(a)):
            c[i][j] = a[j][i]

    return c


def main():
    m1 = [[-1], [2], [3]]
    print(tranps(m1))


if __name__ == '__main__':
    main()
