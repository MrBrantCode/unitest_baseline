"""
QUESTION:
Create two functions, `swap_by_value` and `swap_by_reference`, that swap the values of two variables. The `swap_by_value` function should use a call by value strategy, while the `swap_by_reference` function should use a call by reference strategy. The functions should work with two different types of variables: immutable (e.g., integers) and mutable (e.g., lists). The functions should not modify the original variables when using the call by value strategy, but should modify the original variables when using the call by reference strategy.
"""

def swap_by_value(x, y):
    return y,x

def swap_by_reference(list):
    list[0], list[1] = list[1], list[0]
    return list