"""
QUESTION:
Create a function `outer_function(x)` that returns another function `inner_function(y)` using closure. The `inner_function(y)` should add the value of `x` from the outer function's scope to its argument `y` and return the result. The `outer_function(x)` should be called with an argument `x` and the returned function should be stored in a variable `closure`. The `closure` function should then be called with an argument `y` and the result should be printed.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function