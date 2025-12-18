"""
QUESTION:
Design a function called `Fibonacci` that takes an integer `n` as input and returns the nth number in the Fibonacci sequence, where the sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

def Fibonacci(n):  
    if n == 0:   
        return 0  
    elif n == 1:  
        return 1  
    else:  
        return Fibonacci(n-1) + Fibonacci(n-2)