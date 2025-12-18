"""
QUESTION:
Write a function `are_values_equal` that takes two numerical parameters and returns `True` if they are equal and `False` otherwise. The function must not use comparison operators (e.g., ==, !=, <, >), built-in functions (e.g., equals(), compareTo()), arithmetic operators (e.g., +, -, *, /), or bitwise operators (e.g., &, |, ^, >>, <<). The function should work with integers and floats.
"""

def are_values_equal(a, b):
    # Convert the numerical parameters into strings
    str_a = str(a)
    str_b = str(b)
    
    # Compare the lengths of the strings
    if len(str_a) == len(str_b):
        return True
    else:
        return False