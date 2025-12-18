"""
QUESTION:
Write a function named `fibonacci_sequence` to generate the first `n` numbers in the Fibonacci sequence, where `n` is a given integer. The Fibonacci sequence is a series of numbers in which each number (after the first two) is the sum of the two preceding ones. The input is a positive integer `n`, and the function should return the first `n` numbers in the Fibonacci sequence.
"""

def fibonacci_sequence(n):
    """
    Generate the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci numbers to generate.
    
    Returns:
        list: A list of the first n numbers in the Fibonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq