"""
QUESTION:
Create a function called `maximum(a, b)` that takes two numbers as input and returns the maximum of the two numbers without using any built-in functions or operators for comparison or sorting.
"""

def maximum(a, b):
    # Find the difference between a and b
    diff = a - b
    
    # Check if diff is positive or negative
    # If positive, a is greater than b
    # If negative, b is greater than a
    # If zero, both numbers are equal
    if diff > 0:
        return a
    elif diff < 0:
        return b
    else:
        return a