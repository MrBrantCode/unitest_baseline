"""
QUESTION:
Write a function `compose` that takes two functions as arguments, `f` and `g`, and returns a new function that applies `f` to the result of `g`. The new function should accept a variable number of arguments. Also, write a function `createMultiplier` that takes a number `x` and returns a function that multiplies its argument by `x`. The returned function should maintain a reference to `x`, not its value at the time of creation.
"""

def compose(f, g):
    def wrapper(*args, **kwargs):
        return f(g(*args, **kwargs))
    return wrapper

def createMultiplier(x):
    def multiplier(y):
        return x * y
    return multiplier