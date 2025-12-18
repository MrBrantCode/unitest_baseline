"""
QUESTION:
Create a function named `fibonacci` that calculates the nth Fibonacci number using a for loop and memoization. The function should take an integer `n` as input and return the corresponding Fibonacci number. Additionally, implement a function named `factorial` that calculates the factorial of a given number using recursion. The factorial function should take an integer `n` as input and return the factorial of `n`. The `fibonacci` function should use memoization to optimize the runtime.
"""

def fibonacci(n, fib_dict = {0: 0, 1: 1}):
    """
    Function to compute the Fibonacci value of an integer n using a for loop and memoization.
    """
    if n in fib_dict:
        return fib_dict[n]

    for i in range(2, n + 1):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]
    
    return fib_dict[n]