"""
QUESTION:
Create a function named `swap_variables` that takes two variables as input and swaps their values without using a temporary variable. The function should modify the original variables.
"""

def swap_variables(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b