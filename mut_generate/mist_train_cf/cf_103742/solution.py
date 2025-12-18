"""
QUESTION:
Write a function `sum_of_multiples(num)` that calculates the sum of all numbers up to `num` that are multiples of either 4 or 6. The function should return the calculated sum.
"""

def sum_of_multiples(num):
    """
    Calculates the sum of all numbers up to `num` that are multiples of either 4 or 6.
    
    Args:
        num (int): The upper limit for calculating the sum of multiples.

    Returns:
        int: The calculated sum.
    """
    sum = 0
    for i in range(1, num + 1):
        if i % 4 == 0 or i % 6 == 0:
            sum += i
    return sum