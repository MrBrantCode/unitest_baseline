"""
QUESTION:
Write a function `find_second_largest` that takes a list of numbers as input and returns the second largest number in the list without using any built-in sorting functions. If the list has less than two distinct elements, the function should return the smallest possible value (e.g., negative infinity).
"""

def find_second_largest(nums):
    """
    This function finds the second largest number in a list without using any built-in sorting functions.
    
    Args:
        nums (list): A list of numbers.
    
    Returns:
        The second largest number in the list. If the list has less than two distinct elements, returns negative infinity.
    """
    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    return second_largest