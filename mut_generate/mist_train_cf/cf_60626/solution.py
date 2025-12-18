"""
QUESTION:
Write a function named `fibonacci(n)` that takes a single integer argument `n` and returns the nth Fibonacci number. The function should handle cases where `n` is less than or equal to 0 by printing an error message, and it should return the correct Fibonacci number for `n` greater than 0.
"""

def fibonacci(n):
    if n<=0:
        print("Please enter a positive integer")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        a=0
        b=1
        for i in range(3, n+1):
            a, b = b, a + b
        return b