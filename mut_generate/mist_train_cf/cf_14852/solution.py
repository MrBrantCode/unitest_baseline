"""
QUESTION:
Create a function `fibonacci` that takes an integer `n` as input. The function should return the `n`th term in the Fibonacci series, where each term is the sum of the two preceding ones (starting with 0 and 1). Implement the function using a recursive approach. If `n` is a negative number or zero, the function should return `None`.
"""

def fibonacci(n):
    if n < 1:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)