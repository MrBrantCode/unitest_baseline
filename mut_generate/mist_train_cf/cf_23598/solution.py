"""
QUESTION:
Design a function `fibonacci_up_to_n` to calculate the Fibonacci sequence up to a given number `n`. The function should return a list of Fibonacci numbers that are less than or equal to `n`. The function should not include any Fibonacci numbers that exceed `n`.
"""

def fibonacci_up_to_n(n):
    """
    Calculate the Fibonacci sequence up to a given number n.
    
    Args:
    n (int): The maximum value for the Fibonacci sequence.

    Returns:
    list: A list of Fibonacci numbers less than or equal to n.
    """
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while True:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            if next_fib > n:
                break
            fib_sequence.append(next_fib)
        return fib_sequence