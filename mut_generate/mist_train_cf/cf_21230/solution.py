"""
QUESTION:
Write a function named `fibonacci` to generate the n-th Fibonacci number using recursion. The function should take an integer `n` as input and return the corresponding Fibonacci number. The time complexity of the function should be O(2^n).
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)