"""
QUESTION:
Write a function `Fibonacci(n)` to calculate the nth Fibonacci number, where n is a non-negative integer. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return the correct Fibonacci number for a given n, and handle invalid inputs (negative numbers) by printing an error message.
"""

def Fibonacci(n): 
    """
    Calculate the nth Fibonacci number.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The nth Fibonacci number.

    Note:
    Prints an error message for invalid inputs (negative numbers).
    """
    if n < 0: 
        print("Incorrect input")
        return None  # Return a value to indicate incorrect input
    elif n == 1: 
        return 0
    elif n == 2: 
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2)