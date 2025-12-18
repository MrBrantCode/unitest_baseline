"""
QUESTION:
Write a function called `fibonacci` that generates a list with the first `n` Fibonacci numbers. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. The function should take an integer `n` as input and return a list of the first `n` Fibonacci numbers.
"""

def fibonacci(n):
    """
    Generate a list with the first n Fibonacci numbers.
    """
    fib_list = [0, 1]

    # Generate the list and stop when n is reached
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    return fib_list[:n]