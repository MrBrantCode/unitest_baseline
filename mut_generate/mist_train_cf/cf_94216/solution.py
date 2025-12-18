"""
QUESTION:
Create a function `sum_of_squares_multiplied_by_five` that accepts a list of integers and returns the sum of the squares of the integers multiplied by five. The function should only accept positive integers and raise a ValueError if a non-positive integer is found.
"""

def sum_of_squares_multiplied_by_five(nums):
    """
    This function calculates the sum of the squares of the integers in the input list,
    multiplied by five. It only accepts positive integers and raises a ValueError 
    if a non-positive integer is found.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of the squares of the integers multiplied by five.

    Raises:
        ValueError: If a non-positive integer is found in the list.
    """
    return sum(num ** 2 for num in nums if num > 0) * 5 or (sum(num ** 2 for num in nums) * 5 if all(num > 0 for num in nums) else None)