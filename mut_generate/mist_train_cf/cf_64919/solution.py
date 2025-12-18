"""
QUESTION:
Design a function `calculate_largest_disparity(arr1, arr2)` that takes two numerical arrays of possibly different lengths as input and returns the largest absolute difference between any value in `arr1` and any value in `arr2`. The arrays can contain integers or floating point numbers and may be empty. If either array is empty, the function should return `None`.
"""

def calculate_largest_disparity(arr1, arr2):
    if not arr1 or not arr2:
        return None  # return None if any array is empty
    
    max1, min1 = max(arr1), min(arr1) 
    max2, min2 = max(arr2), min(arr2) 

    return max(abs(max1 - min2), abs(max2 - min1))  # maximum disparity