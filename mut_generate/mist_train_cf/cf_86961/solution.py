"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the nth term of the Fibonacci sequence. The function should use constant space complexity and execute in O(n) time complexity. If `n` is negative, the function should return -1.
"""

def fibonacci(n):
    if n < 0:
        return -1
    
    if n <= 1:
        return n
    
    fib1 = 0
    fib2 = 1
    
    for _ in range(2, n+1):
        fib = fib1 + fib2
        fib2 = fib1
        fib1 = fib
    
    return fib1