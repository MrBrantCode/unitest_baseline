"""
QUESTION:
Write a function named `max_divisible_by_three` to find the maximum value in a given array that is divisible by 3. The function should take an array of integers as input and return the maximum value that meets the condition. If no such value exists, the function should return a default value.
"""

def max_divisible_by_three(arr):
    """
    This function finds the maximum value in a given array that is divisible by 3.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The maximum value in the array that is divisible by 3. If no such value exists, returns None.
    """
    max_divisible = None
    for num in arr:
        if num % 3 == 0:
            if max_divisible is None or num > max_divisible:
                max_divisible = num
    return max_divisible