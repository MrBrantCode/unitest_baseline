"""
QUESTION:
Write a recursive function in Python to generate the nth Fibonacci number, where the function takes an integer n as input and returns the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def entance(n):
    if n <= 1:
       return n
    else:
       return (entance(n-1) + entance(n-2))