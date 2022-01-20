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
        Divide, Halves = WholeA[:mid] and WholeA[mid:]
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

'''
Cited Sources:
Author: Smitha Dinesh Semwal
URL: https://tutorialspoint.dev/algorithm/divide-and-conquer/k-th-element-two-sorted-arrays
Code: 
def kth(arr1, arr2, m, n, k): 

    sorted1 = [0] * (m + n) 
    i = 0
    j = 0
    d = 0
    while (i < m and j < n): 

        if (arr1[i] < arr2[j]): 
            sorted1[d] = arr1[i] 
            i += 1
        else: 
            sorted1[d] = arr2[j] 
            j += 1
        d += 1

    while (i < m): 
        sorted1[d] = arr1[i] 
        d += 1
        i += 1
    while (j < n): 
        sorted1[d] = arr2[j] 
        d += 1
        j += 1
    return sorted1[k - 1] 

# driver code 
arr1 = [2, 3, 6, 7, 9] 
arr2 = [1, 4, 8, 10] 
k = 5; 
print(kth(arr1, arr2, 5, 4, k))
---------------------------------------
Author: Exploration: Divide-and-Conquer Algorithms
Found: Canvas
URL provide by Instructor: https://github.com/DURepo/CS_325_Exercises/blob/main/DivideAndConquer-mergeSort.py
Code:
 def merge_sort(Arr,start,end):
    if(start<end):
        mid = (start+end)//2 #Computes floor of middle value
        merge_sort(Arr,start,mid)
        merge_sort(Arr,mid+1,end)
        merge(Arr,start, mid, end)

def merge(Arr, start, mid, end):
  #temporary arrays to copy the elements of subarray
  leftArray_size = (mid-start)+1
  rightArray_size = (end-mid)

  leftArray = [0]*leftArray_size
  rightArray = [0]*rightArray_size

  for i in range(0, leftArray_size):
    leftArray[i] = Arr[start+i]

  for i in range(0, rightArray_size):
    rightArray[i] = Arr[mid+1+i]

  i=0
  j=0
  k=start

  while (i < leftArray_size and j < rightArray_size):
    if (leftArray[i] < rightArray[j]):
      # filling the original array with the smaller element
      Arr[k] = leftArray[i]
      i = i+1
    else:
      # filling the original array with the smaller element
      Arr[k] = rightArray[j]
      j = j+1
    k = k+1

  # copying remaining elements if any
  while (i<leftArray_size):
    Arr[k] = leftArray[i]
    k = k+1
    i = i+1

  while (j<rightArray_size):
    Arr[k] = rightArray[j]
    k = k+1
    j = j+1


if __name__ == '__main__':
  Arr = [2,14,1,9,10,5,6,18,11]
  merge_sort(Arr, 0, 8)
  print(Arr)
---------------------------------------
Author: Mayank Khanna
URL: https://www.geeksforgeeks.org/merge-sort/
Code: 
if len(arr) > 1:

         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

'''
