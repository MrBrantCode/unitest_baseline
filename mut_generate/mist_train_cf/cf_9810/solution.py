"""
QUESTION:
Create a function named `outer_function` that takes an integer `x` as input, and returns a function that takes another integer `y` as input and returns the sum of `x` and `y`. The returned function should be able to access and use the value of `x` even after `outer_function` has finished executing.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function