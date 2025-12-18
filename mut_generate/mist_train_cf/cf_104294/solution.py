"""
QUESTION:
Write a function called `fibonacci` that calculates the nth Fibonacci number with a time complexity of O(n) without using any additional data structures. The function should take an integer `n` as input and return the corresponding Fibonacci number. If `n` is less than or equal to 0, return "Invalid input".
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number with a time complexity of O(n) without using any additional data structures.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number if n is greater than 0, otherwise "Invalid input".
    """
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b