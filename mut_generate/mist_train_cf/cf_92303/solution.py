"""
QUESTION:
Write a recursive function named `fibonacci` to calculate the nth Fibonacci number. The function should have a time complexity of O(2^n) and use recursion to calculate the result. The function should take an integer `n` as input and return the corresponding Fibonacci number. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)