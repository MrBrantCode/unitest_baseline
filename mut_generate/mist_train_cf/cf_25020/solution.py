"""
QUESTION:
Create a function named `Fibonacci` that generates the nth number in the Fibonacci sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function should take an integer `n` as input and return the corresponding number in the sequence.
"""

def Fibonacci(n):
    """
    Generates the nth number in the Fibonacci sequence.

    Args:
        n (int): The position of the number in the Fibonacci sequence.

    Returns:
        int: The nth number in the Fibonacci sequence.
    """
    f0, f1 = 0, 1

    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        for _ in range(2, n + 1):
            f0, f1 = f1, f0 + f1
        return f1