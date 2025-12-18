"""
QUESTION:
Implement the QuickSort function, which takes a list of integers as input and returns the sorted list. Ensure that the function utilizes the divide-and-conquer strategy through recursion.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)