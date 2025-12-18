"""
QUESTION:
Write a function getFibonacciNumber(n) that returns the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. Implement the function without using recursion or built-in functions, and only use a single loop. The function should take an integer n as input and return an integer as output.
"""

def getFibonacciNumber(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b