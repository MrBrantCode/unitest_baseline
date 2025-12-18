"""
QUESTION:
Write a function `find_min(arr)` that finds the minimum element in a given array. The function should not use any explicit looping constructs or recursive calls in the main program, although it may use implicit recursion within the function itself. The input array is guaranteed to have at least one element.
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