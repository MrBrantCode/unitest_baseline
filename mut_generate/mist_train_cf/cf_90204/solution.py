"""
QUESTION:
Implement a function `quicksort(arr, low, high)` that sorts an array of integers in descending order using the Quicksort algorithm. The function should not use any built-in sorting functions or libraries, have a time complexity of O(n log n), and a space complexity of O(1). The input array may contain duplicate values.
"""

def quicksort(arr, low, high):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] >= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)