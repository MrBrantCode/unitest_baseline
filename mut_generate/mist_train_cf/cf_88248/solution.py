"""
QUESTION:
Design a function `quicksort(arr)` that takes an array `arr` as input and sorts it in-place using the QuickSort algorithm. The function should handle arrays with duplicate elements and have a time complexity of O(n log n) and space complexity of O(1). Do not use any additional data structures or libraries.
"""

def quicksort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1
    
    def sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            sort(arr, low, pi - 1)
            sort(arr, pi + 1, high)
    
    sort(arr, 0, len(arr) - 1)