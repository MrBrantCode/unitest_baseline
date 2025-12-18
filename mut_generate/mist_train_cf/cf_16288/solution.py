"""
QUESTION:
Create a function called `outer_function` that returns another function. This returned function should accept one parameter and return a value that is the sum of this parameter and a value from the outer function's scope. The outer function should accept one parameter that will be used for the summation.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function