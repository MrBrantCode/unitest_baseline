"""
QUESTION:
Create a function `fibonacci(n)` that calculates the nth Fibonacci number using a recursive approach with a time complexity of O(2^n), where n is the inputted index. The function should follow the Fibonacci sequence definition: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)