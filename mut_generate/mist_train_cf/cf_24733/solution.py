"""
QUESTION:
Write a function named `Fibonacci` that calculates the nth Fibonacci number. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should handle cases where `n` is less than 1.
"""

def Fibonacci(n): 
    if n<1: 
        return 0
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)