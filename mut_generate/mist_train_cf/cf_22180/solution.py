"""
QUESTION:
Write a function `sum_excluding_multiples` that calculates the sum of numbers from 1 to n (inclusive), excluding any numbers divisible by both a and b. The function should take three parameters: n, a, and b.
"""

def sum_excluding_multiples(n, a, b):
    """
    Calculate the sum of numbers from 1 to n (inclusive), 
    excluding any numbers divisible by both a and b.

    Parameters:
    n (int): The upper limit of the range.
    a (int): The first divisor.
    b (int): The second divisor.

    Returns:
    int: The sum of the numbers in the range excluding multiples of a and b.
    """
    total = 0
    for num in range(1, n + 1):
        if num % a != 0 or num % b != 0:
            total += num
    return total