"""
QUESTION:
Create a function `sum_n_fibonacci_numbers(n)` that takes an integer `n` as input and returns the sum of the first `n` Fibonacci numbers. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should handle invalid inputs where `n` is less than 0, and return `None` for such cases.
"""

def sum_n_fibonacci_numbers(n):
    """This function takes in a number, n, and sums the first n Fibonacci numbers.
    
    Parameters
    ----------
    n : int
        The number of Fibonacci numbers to sum.
    
    Returns
    -------
    The sum of the first n Fibonacci numbers.
    """
    
    fib = [0, 1]
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            fib.append(fib[i-2] + fib[i-1])
        return sum(fib)