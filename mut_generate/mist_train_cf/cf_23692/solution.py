"""
QUESTION:
Create a function called `Fibonacci(n)` that returns the nth Fibonacci number, where n is a positive integer. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. If n is less than 1, the function should handle this invalid input.
"""

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)