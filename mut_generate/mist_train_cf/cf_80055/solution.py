"""
QUESTION:
Create a function named `f(x)` that takes an integer `x` as input. If `x` is outside the range -100 to 100, recursively reduce or increase `x` by 100 until it falls within this range. Once `x` is within the range -100 to 100, return a value based on whether `x` is positive or negative.
"""

def f(x):
    if x > 100:
        return -1 if f(x - 100) < 0 else 1
    elif x < -100:
        return -1 if f(x + 100) < 0 else 1
    else:
        return -1 if x < 0 else 1