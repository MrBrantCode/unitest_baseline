"""
QUESTION:
Create a function `cube_root_gen` that takes a list of values and returns a generator expression for the cube root values of the numbers in the list, handling negative numbers by applying the cube root to the absolute value and then negating the result. The function should exclude non-integer and non-float values from the list.
"""

def cube_root_gen(lst):
    cube_root = lambda x: x ** (1./3.) if x >= 0 else -(-x) ** (1./3.) 
    return (cube_root(val) for val in lst if isinstance(val, (int, float)))