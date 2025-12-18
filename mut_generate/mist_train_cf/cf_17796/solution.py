"""
QUESTION:
Create a function called `square_even_divisible_by_three` that takes a list of integers as input and returns a new list containing the squares of the even numbers that are also divisible by 3, sorted in descending order. The function should use list comprehension and exclude any numbers that do not meet the specified conditions.
"""

def square_even_divisible_by_three(nums):
    """
    Returns a new list containing the squares of the even numbers 
    that are also divisible by 3, sorted in descending order.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of squares of even numbers divisible by 3.
    """
    return sorted([num ** 2 for num in nums if num % 2 == 0 and num % 3 == 0], reverse=True)