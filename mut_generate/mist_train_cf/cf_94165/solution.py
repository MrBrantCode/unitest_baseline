"""
QUESTION:
Write a function named `outer_function` that accepts one parameter `x` and returns a function `inner_function` that accepts one parameter `y` and returns the sum of `x` and `y`. Ensure that the returned inner function remembers the value of `x` even after the outer function has finished executing.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function