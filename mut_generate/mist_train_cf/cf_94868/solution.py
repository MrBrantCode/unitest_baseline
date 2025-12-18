"""
QUESTION:
Write a function `fibonacci(a, b, n)` to calculate the nth number in a modified Fibonacci sequence that starts with two given numbers `a` and `b`. The function should have a time complexity of O(n).
"""

def fibonacci(a, b, n):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return fibonacci(a, b, n-1) + fibonacci(a, b, n-2)