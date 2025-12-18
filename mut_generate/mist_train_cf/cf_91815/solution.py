"""
QUESTION:
Implement the `inplace_quicksort` function to perform an in-place quicksort on a given array of integers. The function should be able to handle duplicate elements, achieve an average time complexity of O(n log n), and have a space complexity of O(log n). The input array will be modified in-place, and the function should return the sorted array.
"""

def inplace_quicksort(arr):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quicksort(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            quicksort(arr, low, pivot - 1)
            quicksort(arr, pivot + 1, high)

    quicksort(arr, 0, len(arr) - 1)
    return arr