"""
QUESTION:
Write a recursive function named `fibonacci(n)` to calculate the Fibonacci sequence up to the nth number, where n is a positive integer. The function should return a list of the first n Fibonacci numbers. The input n should be a positive integer, and the function should handle invalid inputs (n <= 0) by returning an error message.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be positive."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence