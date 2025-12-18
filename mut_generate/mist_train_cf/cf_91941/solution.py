"""
QUESTION:
Design a function `quickSort(arr)` that takes an array as input, sorts it using the QuickSort algorithm, and handles arrays with duplicate elements. The function should return the sorted array. The input array can contain any type of elements that can be compared using the less-than-or-equal-to operator (<=).
"""

def quickSort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1
    
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    if len(arr) <= 1:
        return arr
    
    index = partition(arr, 0, len(arr) - 1)
    left = quickSort(arr[:index])
    right = quickSort(arr[index+1:])
    
    return left + [arr[index]] + right