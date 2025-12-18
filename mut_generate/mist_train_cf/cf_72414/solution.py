"""
QUESTION:
Write a function named "recursive_abs" that uses recursion to calculate the absolute value of a given number, handling both integers and floating point numbers, without using Python's built-in abs() function.
"""

def recursive_abs(num):
    # Base case: if num is positive or zero, return it
    if num >= 0:
        return num
    # Recursive case: if num is negative, return the absolute value by multiply it by -1 and recurse again
    else:
        return recursive_abs(-num)