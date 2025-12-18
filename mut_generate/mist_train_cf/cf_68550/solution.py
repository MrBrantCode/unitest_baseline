"""
QUESTION:
Write a function named `prod_signs` that takes an array of non-zero integers as input, computes the sum of the magnitudes of distinct integers multiplied by the collective product of signs for each unique number in the array (1 for positive numbers, -1 for negative numbers), and returns the result. If the array is empty or contains a zero, return None.
"""

def prod_signs(arr):
    """
    For a given array arr with non-zero integers, compute the sum of the magnitudes of distinct integers 
    multiplied by the collective product of signs for each unique number in the array, denoted as 1, -1, or 0.
    If the array is empty or contains a zero, return None.
    """
    if not arr or 0 in arr:
        return None
    
    unique_elements = list(set(arr))
    result = 0

    for element in unique_elements:
        result += abs(element) * (1 if element > 0 else -1)
    
    return result