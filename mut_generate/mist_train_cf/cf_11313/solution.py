"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given number using a for loop. The function should take one integer parameter, calculate the factorial by multiplying all positive integers less than or equal to the given number, and return the result. The input number is guaranteed to be a non-negative integer.
"""

def factorial(n):
    """
    Calculate the factorial of a given number using a for loop.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result