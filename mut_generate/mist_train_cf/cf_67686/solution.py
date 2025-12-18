"""
QUESTION:
Implement a function named `swap_variables` that takes two numeric variables as input and swaps their values using bitwise operators without utilizing auxiliary buffer variables.
"""

def swap_variables(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b