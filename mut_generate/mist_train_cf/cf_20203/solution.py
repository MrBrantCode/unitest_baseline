"""
QUESTION:
Write a function `calculate_sum` that takes an integer `number` as input and returns the sum of all multiples of 3 and 5 between 1 and the given number, excluding any multiples that are divisible by both 3 and 5. If the given number is divisible by both 3 and 5, it should also be excluded from the sum.
"""

def calculate_sum(number):
    """
    This function calculates the sum of all multiples of 3 and 5 
    between 1 and the given number, excluding any multiples that 
    are divisible by both 3 and 5.

    Args:
        number (int): The input number up to which the sum is calculated.

    Returns:
        int: The sum of multiples of 3 and 5, excluding multiples of both.
    """
    total = 0
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            continue
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total