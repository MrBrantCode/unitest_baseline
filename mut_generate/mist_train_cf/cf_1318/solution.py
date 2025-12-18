"""
QUESTION:
Create a function named `outer_function` that returns another function, and this returned function accepts two parameters and returns a value that is computed using the values of both parameters. The returned function must be able to access and manipulate the variables from its parent scope.
"""

def outer_function(x):
    def inner_function(y):
        return x + y  
    return inner_function