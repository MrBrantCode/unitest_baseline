"""
QUESTION:
Calculate the sum of all even numbers in a given range.

Create a function `sum_even_numbers` that takes an integer range with a start and end value as input and returns the sum of all even numbers within this range (inclusive). The function should be able to handle any integer range.

Example: For a range of 1 to 100, the output should be the sum of all even numbers within this range.
"""

def sum_even_numbers(start, end):
    """
    This function calculates the sum of all even numbers within a given range (inclusive).
    
    Args:
        start (int): The start of the range.
        end (int): The end of the range.
    
    Returns:
        int: The sum of all even numbers in the range.
    """
    return sum(num for num in range(start, end + 1) if num % 2 == 0)