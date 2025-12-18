"""
QUESTION:
Write a function `find_second_largest` that takes a list of integers as input and returns the second largest number. The function should not use the built-in `max()` or `sorted()` functions. The list may contain duplicate numbers. If the list has less than two distinct numbers, the function should return the smallest possible integer value.
"""

def find_second_largest(lst):
    """
    This function finds the second largest number in a list of integers.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The second largest number in the list. If the list has less than two distinct numbers, returns the smallest possible integer value.
    """
    largest = float('-inf')
    second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest