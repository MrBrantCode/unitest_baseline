"""
QUESTION:
Write a function called `generate_odd_numbers` that takes an integer `n` as input and returns a list of odd numbers between 1 and `n` (inclusive) that are not multiples of 3. The function should return an empty list if no such numbers exist.
"""

def generate_odd_numbers(n):
    """
    Generate a list of odd numbers between 1 and n (inclusive) that are not multiples of 3.

    Args:
    n (int): The upper limit of the range.

    Returns:
    list: A list of odd numbers that are not multiples of 3.
    """
    return [x for x in range(1, n+1) if x % 2 != 0 and x % 3 != 0]