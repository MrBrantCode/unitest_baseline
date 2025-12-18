"""
QUESTION:
Create a function named `recursive_func` that uses recursion to calculate the sum of all numbers from 1 to a given number `n`. The function should have a base case to prevent infinite recursion and a recursive case that calls itself with a decreasing value of `n`. The function should return the calculated sum.
"""

def recursive_func(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_func(n-1)