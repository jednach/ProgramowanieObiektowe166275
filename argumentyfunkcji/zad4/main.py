# zad4

def multiply_ints(*args):
    sum = 1
    for x in args:
        if isinstance(x, int):
            sum *= x
    return sum


def main():
    print(multiply_ints(3, 3.14, 5, "abc", 7))


if __name__ == '__main__':
    main()
