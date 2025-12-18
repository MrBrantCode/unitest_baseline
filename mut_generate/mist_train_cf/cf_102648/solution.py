"""
QUESTION:
Write a function named `fibonacci` that calculates and returns the Fibonacci sequence up to the nth term. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence. The function should also handle invalid input (n <= 0) by returning an error message. Additionally, write a function named `fibonacci_sum` that calculates and returns the sum of all Fibonacci numbers up to the nth term. The function should take an integer `n` as input and return the sum as an integer.
"""

def fibonacci(n):
    """
    Calculates and returns the Fibonacci sequence up to the nth term.

    Args:
    n (int): The nth term of the Fibonacci sequence.

    Returns:
    list: A list of integers representing the Fibonacci sequence up to the nth term.
    """
    # check if n is less than or equal to 0
    if n <= 0:
        return "Invalid input. Please enter a positive integer."

    # initialize the first two terms of the Fibonacci sequence
    fib_seq = [0, 1]

    # calculate the remaining terms of the Fibonacci sequence
    while len(fib_seq) < n:
        next_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)

    return fib_seq

def fibonacci_sum(n):
    """
    Calculates and returns the sum of all Fibonacci numbers up to the nth term.

    Args:
    n (int): The nth term of the Fibonacci sequence.

    Returns:
    int: The sum of all Fibonacci numbers up to the nth term.
    """
    # calculate the Fibonacci sequence
    fib_seq = fibonacci(n)

    # check if fib_seq is a list (i.e., not an error message)
    if isinstance(fib_seq, list):
        # calculate the sum of all Fibonacci numbers up to the nth term
        fib_sum = sum(fib_seq)
        return fib_sum
    else:
        return fib_seq