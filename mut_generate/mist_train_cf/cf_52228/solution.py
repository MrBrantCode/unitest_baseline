"""
QUESTION:
Implement a Closure in Python using a nested function structure. The outer function should take one argument and return the inner function. The inner function should take one argument and return the sum of the argument from the outer function and the argument from the inner function. The returned inner function should be able to access the argument from the outer function even after the outer function has finished its execution.
"""

def entrance(x):
    def inner_function(y):
        return x + y
    return inner_function