"""
QUESTION:
Write a recursive function fib(n) that returns the nth Fibonacci number given a positive integer n, where each Fibonacci number is the sum of the two preceding ones. The function should assume that n is a positive integer and have a time complexity of O(2^n).
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)