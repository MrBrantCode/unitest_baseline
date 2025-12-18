"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number using tail recursion optimization, and explain the concept of tail recursion optimization and its advantages over regular recursion. Your function should take two parameters: the input number `n` and an optional accumulator parameter with a default value of 1. The function should return the factorial of `n` without causing a stack overflow error for large input values.
"""

def entrance(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return entrance(n-1, accumulator * n)