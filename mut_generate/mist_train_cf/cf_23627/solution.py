"""
QUESTION:
Write a function `Fibonacci(n)` that calculates the nth Fibonacci number where `n` is a non-negative integer. The function should return the nth Fibonacci number if `n` is 0 or more, and handle invalid inputs (n < 0) by printing an error message.
"""

def Fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b