"""
QUESTION:
Design a function called `Fibonacci_number(n)` that takes a non-negative integer `n` as input and returns the `n`th number in the Fibonacci sequence, where the sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
"""

def Fibonacci_number(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci_number(n-1) + Fibonacci_number(n-2)