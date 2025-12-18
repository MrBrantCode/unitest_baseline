"""
QUESTION:
Create a function called `fibonacci` that generates and returns the Fibonacci sequence up to the nth number, where n is a given input. The sequence should start with 0 and 1, and each subsequent number is the sum of the two preceding numbers.
"""

def fibonacci(n):
    """
    Generates and returns the Fibonacci sequence up to the nth number.

    Args:
        n (int): The number of terms in the Fibonacci sequence.

    Returns:
        list: A list of integers representing the Fibonacci sequence up to the nth number.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence