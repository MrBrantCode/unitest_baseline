"""
QUESTION:
Write a function `is_geometric_progression(arr)` that determines whether a given array of integers conforms to a geometric progression. The function should return `True` if the array is a geometric progression and `False` otherwise. Assume that the array has at least two elements and does not contain zero.
"""

def is_geometric_progression(arr):
    if len(arr) < 3: 
        return True   
    ratio = arr[1] / arr[0]    
    for i in range(2, len(arr)):
        if arr[i] / arr[i - 1] != ratio:   
            return False
    return True