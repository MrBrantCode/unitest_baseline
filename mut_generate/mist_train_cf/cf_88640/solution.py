"""
QUESTION:
Create a function `fibonacci(n)` that calculates the nth Fibonacci number using recursion. The function should return -1 for negative inputs. The function should have a time complexity of O(2^n) and a space complexity of O(n).
"""

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)