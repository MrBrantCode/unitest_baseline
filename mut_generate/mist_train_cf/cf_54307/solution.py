"""
QUESTION:
Create a function called `fibonacci(n)` that generates the Fibonacci sequence up to the nth number. The function should raise an exception if the input number `n` is less than 0. Additionally, create functions to handle exceptions, display even and odd numbers in the Fibonacci sequence in different colors, reverse the sequence, and compare the computation time of an iterative and recursive solution for the Fibonacci sequence. 

The function should be able to take a positive integer `n` as input and return the Fibonacci sequence as a list of integers. The function should not have any other inputs or side effects other than printing the Fibonacci sequence in different colors and the computation times.
"""

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth number.

    Args:
    n (int): A positive integer.

    Returns:
    list: The Fibonacci sequence as a list of integers.

    Raises:
    Exception: If the input number `n` is less than 0.
    """
    if n < 0:
        raise Exception("Input number must be positive")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_seq = [0, 1]
        while fib_seq[-1] < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq