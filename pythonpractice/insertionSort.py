def insertionSort(arr):
    for i in range(len(arr)):
        tempNumber = arr[i]
        j = i - 1
        while j >= 0 and tempNumber < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tempNumber


def main():
    with open("numbers.txt", "r") as file:
        F = [int(line.strip()) for line in file]
    unSortedArray = F.copy()

    for x in unSortedArray:
        print(x)

    print("------------------")
    insertionSort(unSortedArray)
    for x in unSortedArray:
        print(x)


if __name__ == "__main__":
    main()
