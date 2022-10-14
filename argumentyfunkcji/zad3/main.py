# zad3

def multiply(*args):
    sum = 1
    for x in args:
        sum *= x
    return sum


def main():
    print(multiply(3, 5, 7))


if __name__ == '__main__':
    main()
