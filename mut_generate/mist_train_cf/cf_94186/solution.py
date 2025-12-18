"""
QUESTION:
Implement a function named `sort_array` that takes an array of integers as input and returns the sorted array in ascending order using the quicksort algorithm. The function should handle duplicate elements, have a time complexity of O(nlogn), and not use any additional data structures or libraries. The array can have a maximum length of 10^6.
"""

def sort_array(arr):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            
            quicksort(arr, low, pivot - 1)
            quicksort(arr, pivot + 1, high)

    quicksort(arr, 0, len(arr) - 1)
    return arr