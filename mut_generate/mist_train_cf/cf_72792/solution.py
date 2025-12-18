"""
QUESTION:
Create a function `factorial_array` that takes an array of integers as input and returns a new array where each element is the factorial of the corresponding element in the original array. The input array will contain non-negative integers. Use the `math.factorial` function to calculate factorials.
"""

import math

def factorial_array(arr):
    """
    This function calculates the factorial of each element in the input array.
    
    Args:
    arr (list): A list of non-negative integers.
    
    Returns:
    list: A new list containing the factorials of the input array elements.
    """
    return [math.factorial(i) for i in arr]