"""
QUESTION:
Implement a function `fibonacci(n)` that calculates the nth Fibonacci number, where n is a positive integer. The Fibonacci sequence is defined as: F(1) = 0, F(2) = 1, and F(n) = F(n-1) + F(n-2) for n > 2. If n is less than or equal to 0, the function should return an error message indicating that the input should be a positive integer.
"""

def fibonacci(n):
    if n<=0:
        return "Input should be positive integer"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b