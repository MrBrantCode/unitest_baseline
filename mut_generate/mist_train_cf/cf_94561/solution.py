"""
QUESTION:
Write a function named `sum_arrays` that takes two arrays of integers `a` and `b` as input and returns an array containing the sum of their corresponding elements. The sum should be calculated up to the length of the shorter array if `a` and `b` have different lengths.
"""

def sum_arrays(a, b):
    """
    This function takes two arrays of integers as input and returns an array containing 
    the sum of their corresponding elements. The sum is calculated up to the length of 
    the shorter array.

    Args:
        a (list): The first array of integers.
        b (list): The second array of integers.

    Returns:
        list: A list of integers representing the sum of corresponding elements from a and b.
    """
    result = []
    for i in range(min(len(a), len(b))):
        result.append(a[i] + b[i])
    return result