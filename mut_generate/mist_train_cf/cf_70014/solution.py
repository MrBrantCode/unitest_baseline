"""
QUESTION:
Create a function named `fibonacci_sequence` that generates a Fibonacci sequence up to a given number `y`. The sequence should start with 0 and 1, and each subsequent number should be the sum of the previous two numbers. The function should return the sequence as a list of integers and stop generating numbers when the next number in the sequence would exceed the given value `y`.
"""

def fibonacci_sequence(y):
    """
    Generate a Fibonacci sequence up to a given number y.
    
    Args:
        y (int): The maximum value in the Fibonacci sequence.
    
    Returns:
        list: A list of integers representing the Fibonacci sequence up to y.
    """
    fibonacciSeries = [0, 1]
    while (fibonacciSeries[-1] + fibonacciSeries[-2]) <= y:
        fibonacciSeries.append(fibonacciSeries[-1] + fibonacciSeries[-2])
    return fibonacciSeries