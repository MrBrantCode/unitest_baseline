"""
QUESTION:
Write a recursive function named Fibonacci that takes an integer n as input and returns the nth Fibonacci number. The Fibonacci sequence is defined by the recurrence relation: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. The function should not use any loops or iterative methods and should only rely on recursive calls.
"""

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)