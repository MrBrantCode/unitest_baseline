"""
QUESTION:
Design a recursive function named `fibonacci_squares(n)` that takes a non-negative integer `n` as input and returns a tuple containing the nth Fibonacci number and the sum of the squares of the Fibonacci sequence up to the nth term. The function should not use any global variables or loops, and it should handle negative input by returning an error message.
"""

def fibonacci_squares(n):
    """
    This function computes the nth Fibonacci number and the sum of squares of the Fibonacci sequence up to the nth term.
    
    Args:
    n (int): The position of the Fibonacci number in the sequence.
    
    Returns:
    tuple: A tuple containing the nth Fibonacci number and the sum of squares of the Fibonacci sequence up to the nth term.
    """
    
    # Recursion base cases
    if n < 0:
        return "Error: input number should be non-negative."
    elif n == 0:
        return (0, 0)
    elif n == 1:
        return (1, 1)

    # Recursively compute the (n-1)th and (n-2)th Fibonacci numbers and their squares' sum.
    else:
        (fib_n_minus_2, sum_squares_n_minus_2) = fibonacci_squares(n-2)
        (fib_n_minus_1, sum_squares_n_minus_1) = fibonacci_squares(n-1)
        fib_n = fib_n_minus_2 + fib_n_minus_1
        sum_squares_n = sum_squares_n_minus_1 + fib_n ** 2

    return (fib_n, sum_squares_n)