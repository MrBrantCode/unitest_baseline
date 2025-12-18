"""
QUESTION:
Write a function called fibonacci(n) that finds the nth number in the Fibonacci sequence. The function should not use any loops, memoization techniques, or built-in functions, and should have a time complexity of O(2^n). The function should not use any additional data structures or global variables and should handle negative input numbers by returning None.
"""

def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)