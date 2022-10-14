# zad2
def mult_ints(a):
    sum = 1
    for x in a:
        if isinstance(x, int):
            sum *= x
    return sum


def main():
    print(mult_ints([3, 3.14, 5, "abc", 7]))


if __name__ == '__main__':
    main()
