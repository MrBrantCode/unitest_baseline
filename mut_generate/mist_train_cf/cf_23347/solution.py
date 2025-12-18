"""
QUESTION:
Write a function `nth_fibonacci(n)` that calculates the nth Fibonacci number, where the sequence is defined as: F(0) = F(1) = 1 and F(n) = F(n-1) + F(n-2) for n > 1. The input integer n is the position of the Fibonacci number to be found.
"""

def nth_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        n1, n2 = 1, 1
        for i in range(2, n):
            n1, n2 = n2, n1 + n2
        return n2