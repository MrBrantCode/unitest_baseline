"""
QUESTION:
Create a function named `Fibonacci` that calculates and returns the nth Fibonacci number. The function should take one integer argument `x`, where `x` represents the position of the Fibonacci number to be calculated. The function should use recursion and return the calculated Fibonacci number. The Fibonacci sequence is defined as follows: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
"""

def Fibonacci(x): 
    if x == 0: 
        return 0
    elif x == 1: 
        return 1
    else: 
        return Fibonacci(x-1)+Fibonacci(x-2)