"""
QUESTION:
Write a function `sum_of_evens` that calculates the sum of squares of even numbers from a given range, excluding the number 4. The function should take two parameters: `start` and `end`, representing the start and end of the range respectively.
"""

def sum_of_evens(start, end):
    """
    This function calculates the sum of squares of even numbers 
    from a given range, excluding the number 4.

    Args:
    start (int): The start of the range.
    end (int): The end of the range.

    Returns:
    int: The sum of squares of even numbers in the given range.
    """
    sum_of_evens = 0
    for num in range(start, end + 1):
        if num != 4 and num % 2 == 0:
            sum_of_evens += num ** 2
    return sum_of_evens