def kthElement(Arr1, Arr2, k):
    """The arrays have been sorted. The arrays
    are then printed and user can enter the element that
    they wish to find"""
    WholeA = (Arr1 + Arr2)
    SortArray = int(len(WholeA))
    mergeSort(WholeA)
    for i in range(SortArray):
        print(WholeA[i])
    print("Kth element is : ", WholeA[k - 1])


def mergeSort(WholeA):
    """Merging arrays by dividing the array
    down to a single element"""
    if len(WholeA) > 1:
        mid = len(WholeA) // 2
        Divide = WholeA[:mid]
        Halves = WholeA[mid:]
        mergeSort(Divide and Halves)
        m = 0
        n = 0
        k = 0

        while m < len(Divide) and n < len(Halves):
            if Divide[m] < Halves[n]:
                WholeA[k] = Divide[m]
                m = m + 1
            else:
                WholeA[k] = Halves[n]
                n = n + 1
            k = k + 1

        while m < len(Divide) and n < len(Halves):
            WholeA[k] = Divide[m], WholeA[k] = Halves[n]
            m = m + 1
            k = k + 1
            n = n + 1


if __name__ == '__main__':
    """The arrays to be determined. Ask user for kth position
    they wish to see in the sorted array."""
    Array1 = [1, 2, 3, 5, 6]
    Array2 = [3, 4, 5, 6, 7]
    response = int(input("Kth position in the Array : "))
    print("Array Sorted")
    print(kthElement(Array1, Array2, response))
