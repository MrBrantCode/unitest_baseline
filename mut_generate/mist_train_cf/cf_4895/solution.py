"""
QUESTION:
Implement a recursive quicksort function that sorts an array of integers with a time complexity of O(nlogn) in all cases. The function should not use any built-in sorting functions or libraries. Ensure that the pivot element is correctly placed in its final sorted position to avoid infinite loops. The function should take one argument, an array of integers, and return the sorted array.
"""

def entrance(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return entrance(left) + middle + entrance(right)