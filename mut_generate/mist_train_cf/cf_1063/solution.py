"""
QUESTION:
Implement a function named `multiply` that demonstrates the concept of closures and partial function application. The function should take an argument `x` and return another function that multiplies its argument by `x`. The returned function should remember the value of `x` even after the `multiply` function has finished executing.
"""

def multiply(x):
    def inner_function(y):
        return x * y
    return inner_function