"""
QUESTION:
Implement a `quickSort` function that sorts an array of integers in ascending order. The function should take one argument, `arr`, which is the list of integers to be sorted. The function should return the sorted list. The input array can be of any length, but the function should be able to handle empty or single-element arrays.
"""

def quick_sort(arr):
    if len(arr) <= 1: 
        return arr
    pivot = arr.pop()
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)