"""
QUESTION:
Implement a function named `quickSort` that takes a list of numbers as input and returns the sorted list using the quick sort algorithm. The function should handle lists of any length, including empty lists.
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