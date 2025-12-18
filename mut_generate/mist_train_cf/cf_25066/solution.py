"""
QUESTION:
Create a function `fibonacci_sequence` to generate the first n numbers in the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `n` as input and return a list of the first n numbers in the sequence.
"""

def fibonacci_sequence(n):
    """
    Generate the first n numbers in the Fibonacci sequence.
    
    Args:
    n (int): The number of Fibonacci numbers to generate.
    
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
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence