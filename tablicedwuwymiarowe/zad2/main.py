# zad2
def main():
    arr1 = []
    for x in range(10):
        arr1.append([i for i in range(1, x + 2)])
    print(arr1)
    sum1 = 0
    for x in range(10):
        sum1 += sum(arr1[x])
        print(sum(arr1[x]))
    print(sum1)


if __name__ == '__main__':
    main()
