"""
QUESTION:
Write a function named `divide_list` that takes a list of integers `numbers` and an integer `divisor` as input. For each number in the list, calculate the quotient and remainder when divided by the divisor, rounding quotients of negative numbers towards negative infinity. Return a list of tuples, where each tuple contains the quotient and remainder for the corresponding number in the input list.
"""

def divide_list(numbers, divisor):
    """
    Calculate the quotient and remainder for each number in the list when divided by the divisor.

    Args:
        numbers (list): A list of integers.
        divisor (int): The number by which to divide each integer in the list.

    Returns:
        list: A list of tuples, where each tuple contains the quotient and remainder for the corresponding number in the input list.
    """
    result = []
    for number in numbers:
        quotient, remainder = divmod(number, divisor)
        result.append((quotient, remainder))
    return result