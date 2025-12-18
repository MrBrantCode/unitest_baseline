"""
QUESTION:
Write a function `outer_function` that takes one argument and returns another function `inner_function`. The `inner_function` should take one argument and return the sum of its argument and the argument of `outer_function`. The returned `inner_function` should have access to the argument of `outer_function` even after `outer_function` has finished executing.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function