"""
QUESTION:
Write a function named `divisors` that takes a number as input and returns a list of its divisors, excluding the number itself.
"""

def divisors(num):
    """
    Returns a list of divisors of the input number, excluding the number itself.

    Args:
    num (int): The number for which divisors are to be found.

    Returns:
    list: A list of divisors of the input number.
    """
    return [i for i in range(1, num) if num % i == 0]