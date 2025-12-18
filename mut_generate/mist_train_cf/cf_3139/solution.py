"""
QUESTION:
Create a function called `check_equality` that takes two numerical parameters `a` and `b` and returns `True` if they are equal and `False` otherwise, without using any comparison operators, built-in functions, arithmetic operators, bitwise operators, loops, or recursion.
"""

def check_equality(a, b):
    diff = a - b
    return not diff