"""
QUESTION:
Write a function named `Fibonacci(n)` that calculates the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return the nth number in this sequence. Assume n is a non-negative integer. If n is negative, the function should print "Incorrect input".
"""

def Fibonacci(n): 
    a = 0
    b = 1
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return a 
    elif n==1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
    return b