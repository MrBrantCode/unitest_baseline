"""
QUESTION:
Write a function `fibonacci_power_sequence` that generates the Fibonacci sequence up to the given positive integer `n` (greater than 1). Each Fibonacci number in the sequence should be raised to the power of 4 and multiplied by 3.
"""

def fibonacci_power_sequence(n):
    """
    Generates the Fibonacci sequence up to the given positive integer `n` (greater than 1).
    Each Fibonacci number in the sequence is raised to the power of 4 and multiplied by 3.

    Args:
        n (int): The number up to which the Fibonacci sequence is generated.

    Returns:
        list: A list of Fibonacci numbers raised to the power of 4 and multiplied by 3.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return [3 * num ** 4 for num in fib_sequence]