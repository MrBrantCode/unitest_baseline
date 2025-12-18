"""
QUESTION:
Create a function `fibonacci(n)` to calculate the nth Fibonacci number, then use this function to print the first 1000 Fibonacci numbers, one per line, and calculate their sum. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should handle cases where n is 0, 1, or greater than 1.
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, 
    usually starting with 0 and 1.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]