"""
QUESTION:
Given a list of integers, write a function named `process_numbers` that takes the list as input, squares each number, subtracts 1 from the result, and returns a list of numbers that are greater than 5. The solution should be implemented using a list comprehension and should be easy to understand for human readers.
"""

def process_numbers(nums):
    """
    This function takes a list of integers, squares each number, subtracts 1 from the result, 
    and returns a list of numbers that are greater than 5.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of numbers greater than 5 after squaring and subtracting 1.
    """
    return [n**2 - 1 for n in nums if n**2 - 1 > 5]