"""
QUESTION:
Create a function `fibonacci(n)` that finds the nth number in the Fibonacci sequence. The function should take an integer `n` as input and return the corresponding Fibonacci number. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1. If `n` is less than 0, the function should print "Incorrect input".
"""

def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)