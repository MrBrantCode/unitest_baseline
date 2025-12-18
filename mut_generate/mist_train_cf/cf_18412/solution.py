"""
QUESTION:
Write a function `fibonacci_sum` that calculates the sum of the first n numbers in the Fibonacci sequence, where each number is multiplied by its corresponding index in the sequence. The function should take an integer n as input and return the calculated sum. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
"""

def fibonacci_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence, 
    where each number is multiplied by its corresponding index in the sequence.

    Args:
        n (int): The number of terms in the Fibonacci sequence.

    Returns:
        int: The sum of the first n numbers in the Fibonacci sequence, 
             each multiplied by its corresponding index.
    """
    a, b = 0, 1
    total = 0
    for i in range(1, n + 1):
        total += a * i
        a, b = b, a + b
    return total