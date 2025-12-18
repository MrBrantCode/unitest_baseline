"""
QUESTION:
Write a function `generate_fibonacci_numbers` that generates a list of Fibonacci numbers up to the nth number in the sequence. The input should be a positive integer n, and the output should be a list of Fibonacci numbers.
"""

def generate_fibonacci_numbers(n):
    """
    Generates a list of Fibonacci numbers up to the nth number in the sequence.

    Args:
        n (int): A positive integer representing the position of the Fibonacci number in the sequence.

    Returns:
        list: A list of Fibonacci numbers up to the nth number in the sequence.
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