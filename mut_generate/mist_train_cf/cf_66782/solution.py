"""
QUESTION:
Implement the quicksort function, which sorts an array of elements in ascending order using the QuickSort algorithm. The function should take an array of integers as input and return the sorted array. The time complexity of the function should be O(n log n) on average.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)