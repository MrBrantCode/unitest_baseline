"""
QUESTION:
Write a function `power_sum` that takes an array of integers as input and returns the sum of the 3rd and 5th elements raised to the power of the 2nd element. The array is 0-indexed.
"""

def power_sum(arr):
    """
    This function takes an array of integers as input and returns the sum of the 3rd and 5th elements raised to the power of the 2nd element.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of the 3rd and 5th elements raised to the power of the 2nd element.
    """
    return (arr[2] + arr[4]) ** arr[1]