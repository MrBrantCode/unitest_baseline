"""
QUESTION:
Implement a function `Fibonacci(n)` to calculate the nth Fibonacci number, where the Fibonacci sequence is defined as the series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. The function should be recursive and only return the nth Fibonacci number.
"""

def entrance(n):
    if n == 0 or n == 1:
        return n 
    else: 
        return entrance(n-1) + entrance(n-2)