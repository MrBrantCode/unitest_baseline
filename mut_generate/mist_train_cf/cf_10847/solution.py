"""
QUESTION:
Implement the `quick_sort` function to sort an array of integers in-place using the quick sort algorithm. The function should take an array of integers `arr` as input, where 1 <= len(arr) <= 10^5 and -10^6 <= arr[i] <= 10^6, and sort the array in-place.
"""

def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def quick_sort_helper(low, high):
        if low < high:
            pivot = partition(low, high)
            quick_sort_helper(low, pivot - 1)
            quick_sort_helper(pivot + 1, high)

    quick_sort_helper(0, len(arr) - 1)