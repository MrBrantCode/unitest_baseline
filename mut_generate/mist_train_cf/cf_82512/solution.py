"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number, where n can be a positive or negative integer. If n is negative, the function should return the corresponding Fibonacci number from the end of the sequence, with the sign determined by the parity of n (positive for odd n and negative for even n).
"""

def fibonacci(n):
    if n==0:
        return 0
    elif n==1 or n==-1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        fib = fibonacci(-n)
        return -fib if n % 2 == 0 else fib