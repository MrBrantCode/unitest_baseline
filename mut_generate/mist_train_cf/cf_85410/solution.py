"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number `n`. Then, use this function to find the factorial of each prime number in the list. The input list only contains prime numbers. The function should be able to handle numbers in the given list.
"""

def factorial(n):
    """
    This function calculates the factorial of a number.
    
    Args:
    n (int): A non-negative integer.
    
    Returns:
    int: The factorial of n.
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)