"""
QUESTION:
Create a function called `outer_function` that accepts one parameter, contains at least one inner function, and returns a closure. The closure function should take at least two parameters and return a value that is computed using the values of both parameters. The inner function should manipulate the values of the parameters in a non-trivial way before returning the final computed value.
"""

def outer_function(x):
    def inner_function(y, z):
        return (x + y) * z  # Manipulating the values of x, y, and z
        
    return inner_function