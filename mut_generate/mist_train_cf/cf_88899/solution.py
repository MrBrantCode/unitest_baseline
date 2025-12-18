"""
QUESTION:
Write a function named `outer_function` that takes an integer `x` and returns another function `inner_function` that adds `x` to its argument `y` and returns the result. The function should demonstrate the concept of closures in Python, where the returned function retains the value of `x` even after the `outer_function` has finished executing.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function