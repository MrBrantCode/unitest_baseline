"""
QUESTION:
Create a function called `quick_sort` that uses the Quick Sort algorithm to sort a given list of numerical values in ascending order. The function should work for lists containing any number of elements and should handle duplicate values.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)