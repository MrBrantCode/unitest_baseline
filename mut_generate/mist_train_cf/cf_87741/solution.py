"""
QUESTION:
Implement a function called `outer_function` that takes one argument and returns a closure containing at least three nested functions, each with their own parameters and return values. Ensure the closure demonstrates the usage of higher-order functions and currying. The function should be able to maintain state even after the outer function has finished executing. The function should not take any additional arguments other than the one specified.
"""

def outer_function(x):
    def inner_function(y):
        def nested_function(z):
            return x + y + z
        return nested_function
    return inner_function