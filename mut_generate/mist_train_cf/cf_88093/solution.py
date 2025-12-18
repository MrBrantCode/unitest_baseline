"""
QUESTION:
Implement the factorial2 function that calculates the factorial of a non-negative integer n using recursion without any loops or additional helper functions. The function should take an integer n as input and return the factorial of n.
"""

def factorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial2(n-1)