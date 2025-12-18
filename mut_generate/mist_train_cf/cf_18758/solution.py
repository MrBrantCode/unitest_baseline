"""
QUESTION:
Design a function named `quickSort` that takes an array as input and sorts it using the QuickSort algorithm, handling arrays with duplicate elements. The function should have a time complexity of O(n log n) and a space complexity of O(log n).
"""

def quickSort(arr):
    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1

        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i + 1

    def sort(arr, left, right):
        if left < right:
            pivotIndex = partition(arr, left, right)
            sort(arr, left, pivotIndex - 1)
            sort(arr, pivotIndex + 1, right)

    sort(arr, 0, len(arr) - 1)