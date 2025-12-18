"""
QUESTION:
Write a function named `outer_function` that demonstrates the usage of closures in Python. The function should take one argument `x` and return another function `inner_function` that takes one argument `y` and returns the sum of `x` and `y`. Provide an explanation of the concept of closures and the usage of the function, including common challenges and strategies for debugging.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function