"""
QUESTION:
Write a function `fibonacci` to generate the nth Fibonacci number. The function should take an integer `n` as input and return a string representing the corresponding Fibonacci number. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
"""

def fibonacci(n):
    """
    Generate the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    str: A string representing the corresponding Fibonacci number.
    """
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        fibonaccinumbers = [0, 1]
        for i in range(2, n + 1):
            fibonaccinumbers.append(fibonaccinumbers[i - 1] + fibonaccinumbers[i - 2])

        return str(fibonaccinumbers[n])