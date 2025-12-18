"""
QUESTION:
Create a function named `lexical_closure` that takes one argument and returns a function. The returned function should take one argument and return the sum of the two arguments. The returned function should be able to remember the value of the argument passed to the outer function even after the outer function has finished executing.
"""

def lexical_closure(x):
    def inner_function(y):
        return x + y
    return inner_function