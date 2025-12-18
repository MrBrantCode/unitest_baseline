"""
QUESTION:
Design a recursive function called `fibonacci` that calculates the Fibonacci sequence up to `n` numbers, where `n` is a positive integer. The function should return a list of Fibonacci numbers. Implement the function with a base case to handle invalid or non-positive inputs, and a recursive case to generate the sequence. Consider the benefits and limitations of recursion in the implementation.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n-1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list