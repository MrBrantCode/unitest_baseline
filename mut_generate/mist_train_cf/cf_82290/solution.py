"""
QUESTION:
Create a function `binary_search(array, target)` that performs a binary search on a sorted list of distinct integers. The list can contain negative numbers and integers between 1 and 1,000,000. The function should return the index of the target integer if found, and -1 if not found.
"""

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break       
            lower = x
        else:
            upper = x
    return -1  # If not found