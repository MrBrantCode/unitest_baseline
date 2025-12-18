"""
QUESTION:
Create a function called `outer_function` that takes an integer `x` and returns a function. The returned function, when called with an integer `y`, should return the sum of `x` and `y`. The returned function should retain the value of `x` even after `outer_function` has finished executing.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function