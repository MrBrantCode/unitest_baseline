"""
QUESTION:
Create a function named `outer_function` that takes an argument `x` and returns another function `inner_function` that takes an argument `y`. The returned function should have access to `x` from its enclosing scope and return the sum of `x` and `y`.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function