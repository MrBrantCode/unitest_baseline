"""
QUESTION:
Write a function named `fibonacci_sequence` that takes a positive integer `n` greater than 1 as input. The function should return the Fibonacci sequence up to the nth number, where each Fibonacci number is raised to the power of 3 and multiplied by 2. The input `n` will be a positive integer greater than 1.
"""

def fibonacci_sequence(n):
    """
    Returns the Fibonacci sequence up to the nth number, 
    where each Fibonacci number is raised to the power of 3 and multiplied by 2.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        list: The Fibonacci sequence up to the nth number.
    """
    sequence = [2, 2]
    a, b = 2, 2
    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(2 * (b ** 3))
    return sequence