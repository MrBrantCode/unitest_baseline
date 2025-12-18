"""
QUESTION:
Write a function named `find_median` that takes three numbers as input and returns their median without using any conditional statements (if, elif, else) or comparison operators (>, <, ==). The function should rely solely on mathematical operations and functions.
"""

def find_median(a, b, c):
    return (a + b + c) - max(a, b, c) - min(a, b, c)