"""
QUESTION:
Implement a function `find_min(arr)` that takes an array of integers as input and returns the minimum element in the array without using explicit looping constructs or recursive calls in the main program.
"""

def find_min(arr):
    n = len(arr)
    
    # Base case: if array has only one element, it is the minimum
    if n == 1:
        return arr[0]
    
    # Divide the array into two halves
    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Find minimum element in each half
    min_left = find_min(left_half)
    min_right = find_min(right_half)
    
    # Compare and return the smaller minimum element
    return min(min_left, min_right)