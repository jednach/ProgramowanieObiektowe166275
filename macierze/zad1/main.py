# zad1
def sum(a, b):
    if (len(a) != len(b)) or (len(a[0]) != len(b[0])):
        print("operacja nie jest możliwa")
        return
    c = [[0]*len(a[0]) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]
    return c

def main():
    m1 = [[-1, 0], [2, 1]]
    m2 = [[1, 0], [2, 3]]
    print(sum(m1, m2))

if __name__ == '__main__':
    main()
