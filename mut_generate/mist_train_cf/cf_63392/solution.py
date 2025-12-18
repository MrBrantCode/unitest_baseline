"""
QUESTION:
Implement a function `quickSort(arr, low, high)` that sorts the array `arr` in ascending order using the Quick Sort algorithm. The function should take an array `arr` and two indices `low` and `high` as input, and recursively sort the array in-place without using any extra space. The partition scheme used should be the Lomuto partition scheme, where the last element is chosen as the pivot.
"""

def quickSort(arr, low, high):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)