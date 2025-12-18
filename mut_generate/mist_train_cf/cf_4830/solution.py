"""
QUESTION:
Write a function `find_second_largest` that takes a list of integers as input and returns the second largest number in the list without using the built-in `max()` or `sorted()` functions. The function should handle the case when the list contains duplicate numbers. If the list has less than two unique numbers, the function should return the lowest possible integer value.
"""

def find_second_largest(lst):
    """
    This function finds the second largest number in a list of integers.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    int: The second largest number in the list. If the list has less than two unique numbers, returns the lowest possible integer value.
    """
    largest = lst[0]
    second_largest = float('-inf')
    
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest