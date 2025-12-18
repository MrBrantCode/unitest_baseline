"""
QUESTION:
Write a function named `fibonacci(n)` that calculates the nth Fibonacci number using recursion. The function should take an integer `n` as input and return the corresponding Fibonacci number. Analyze the time complexity of the function, considering the repetitions in computation and the expansion of recursive calls.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)