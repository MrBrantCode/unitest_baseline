"""
QUESTION:
Implement a function called `inplace_quicksort` that takes an array as input, sorts it in-place using the quicksort algorithm, and returns the sorted array. The function should handle duplicate elements and have an average time complexity of O(n log n) and a space complexity of O(log n).
"""

def inplace_quicksort(arr):
    def partition(low, high):
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

    def quicksort(low, high):
        if low < high:
            pivot = partition(low, high)
            quicksort(low, pivot - 1)
            quicksort(pivot + 1, high)

    quicksort(0, len(arr) - 1)
    return arr