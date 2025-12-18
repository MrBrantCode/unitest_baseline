"""
QUESTION:
Create a function `outer_function` that takes an integer `x` and returns another function `inner_function` that takes an integer `y` and returns the sum of `x` and `y`. The inner function should have access to `x` even after `outer_function` has finished executing.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function