"""
QUESTION:
Create a function named Fibonacci(n) that generates the nth number in the Fibonacci sequence, where n is a non-negative integer. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should handle invalid inputs by printing an error message.
"""

def Fibonacci(n): 
    if n < 0: 
        print("Incorrect input") 
    elif n == 1: 
        return 0
    elif n == 2: 
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2)