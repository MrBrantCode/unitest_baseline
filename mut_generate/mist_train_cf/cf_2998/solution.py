"""
QUESTION:
Implement a closure named `outer_function` that contains at least three nested functions, each with their own parameters and return values. Ensure the closure is created by returning an inner function that references variables from its parent function.
"""

def outer_function(x):
    def inner_function(y):
        def nested_function(z):
            return x + y + z
        return nested_function
    return inner_function