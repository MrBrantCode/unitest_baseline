"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number using recursion, where n is a non-negative integer. The function should return the nth Fibonacci number. If n is less than 0, it should print an error message. The Fibonacci sequence is defined as: F(1) = 0, F(2) = 1, and F(n) = F(n-1) + F(n-2) for n > 2.
"""

def fibonacci(n): 
    if n<0: 
        print("Incorrect input")
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)