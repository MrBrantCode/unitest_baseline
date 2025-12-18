"""
QUESTION:
Create a function `transform_numbers` that takes a list of integers as input. For each number in the list, if the number is even, square it; if the number is odd, add one. Return a new list containing the transformed numbers in the same order as the original list.
"""

def transform_numbers(nums):
    """
    This function transforms a list of integers by squaring even numbers and adding one to odd numbers.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A new list containing the transformed numbers.
    """
    return [num**2 if num%2==0 else num+1 for num in nums]