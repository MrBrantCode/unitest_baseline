"""
QUESTION:
Write a function named `sortString` that takes a list of at least two floating-point numbers as input and returns the list sorted in descending order. The function should correct the existing implementation to ensure the output is always in descending order, regardless of the input.
"""

def sortString(s):
    s.sort(reverse=True)
    return s