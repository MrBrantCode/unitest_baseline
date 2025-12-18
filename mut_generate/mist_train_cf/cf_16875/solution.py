"""
QUESTION:
Write a function called `quickSort` that takes in an integer array `arr` and its size `n` as parameters, and sorts the elements of `arr` in ascending order using the Quick Sort algorithm. The pivot element should be chosen as the median of the first, middle, and last elements of the array. The array size will always be odd. The function should return the sorted array.
"""

def quickSort(arr, n):
    def partition(arr, low, high):
        pivot = getMedianPivot(arr, low, high)
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def findMedian(arr, low, high):
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        return mid

    def getMedianPivot(arr, low, high):
        mid = findMedian(arr, low, high)
        arr[mid], arr[high] = arr[high], arr[mid]
        return arr[high]

    def quickSortUtil(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            quickSortUtil(arr, low, pivot - 1)
            quickSortUtil(arr, pivot + 1, high)

    quickSortUtil(arr, 0, n - 1)
    return arr