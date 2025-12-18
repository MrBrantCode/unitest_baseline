"""
QUESTION:
Implement a function named `quicksort` that sorts a list of integers in ascending order using the quicksort algorithm. The function should take a list of integers as input and return a new sorted list. The input list can be of any length, including zero or one element.
"""

def quicksort(arr): 
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)