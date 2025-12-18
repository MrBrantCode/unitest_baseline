"""
QUESTION:
Write a function named `fibonacci(n)` that takes an integer `n` as input and returns the `n`-th Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should handle the cases where `n` is 0 or 1, which correspond to the first two numbers in the Fibonacci sequence.
"""

def fibonacci(n): 
    a = 0
    b = 1
    
    if n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b