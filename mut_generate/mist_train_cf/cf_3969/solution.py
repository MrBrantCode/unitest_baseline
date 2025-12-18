"""
QUESTION:
Implement a function `quicksort(arr)` that sorts an array using the QuickSort algorithm. The function should handle arrays with duplicate elements, have a time complexity of O(n log n), and a space complexity of O(1) without using any additional data structures or libraries. The function should modify the given array in-place and return the sorted array.
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
    return arr