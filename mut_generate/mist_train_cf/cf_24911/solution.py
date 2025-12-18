"""
QUESTION:
Implement a function `quickSort(arr)` that takes an array of integers as input and returns a new sorted array using the Quick Sort algorithm. The function should not modify the original array and should handle arrays of any length, including empty arrays.
"""

def quickSort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)