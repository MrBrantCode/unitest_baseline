"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number using an iterative approach with constant space complexity. The function should handle cases where n is less than or equal to 0, and it should return `None` for these cases. For n greater than 0, the function should return the nth Fibonacci number, where the Fibonacci sequence is defined as 0, 1, 1, 2, 3, 5, 8, and so on.
"""

def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    fib1, fib2 = 0, 1
    for _ in range(3, n+1):
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
    
    return fib2