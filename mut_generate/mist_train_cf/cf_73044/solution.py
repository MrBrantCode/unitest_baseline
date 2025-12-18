"""
QUESTION:
Create a function named `find_max_of_three` that takes three numerical arguments `a`, `b`, and `c`, and returns the largest among them without using built-in max function.
"""

def find_max_of_three(a, b, c):
    if a > b:
        max_ab = a
    else:
        max_ab = b
    if c > max_ab:
        return c
    else:
        return max_ab