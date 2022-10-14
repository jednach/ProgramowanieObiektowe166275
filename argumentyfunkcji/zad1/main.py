# zad1
def mult(a):
    sum = 1
    for x in a:
        sum *= x
    return sum


def main():
    print(mult([3, 5, 7]))
    print(mult(range(1, 8, 2)))


if __name__ == "__main__":
    main()
