"""
QUESTION:
Design a function that generates the sum of the squares of the Fibonacci sequence up to n elements. The function should also return all Fibonacci sequences and their squares up to n. The input integer n should not exceed 50.
"""

def fibonacci_squares_sum(n):
    """
    This function generates the sum of the squares of the Fibonacci sequence up to n elements.
    It also returns all Fibonacci sequences and their squares up to n.

    Args:
        n (int): The number of elements in the Fibonacci sequence.

    Returns:
        list: A list of Fibonacci numbers up to n elements.
        list: A list of squares of Fibonacci numbers up to n elements.
        int: The sum of the squares of Fibonacci numbers up to n elements.
    """

    # Create an empty list to store Fibonacci series
    fib_series = [0, 1]
    
    # Generate the Fibonacci series up to n elements
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    # Create an empty list to store squares of Fibonacci elements
    squares = [num ** 2 for num in fib_series]
    
    # Compute the sum of squares
    sum_squares = sum(squares)
    
    return fib_series, squares, sum_squares