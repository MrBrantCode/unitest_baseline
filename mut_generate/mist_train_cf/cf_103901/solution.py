"""
QUESTION:
Create a function called `increment(x)` that takes an integer `x` as input, increments it by 1, and recursively calls itself if the incremented value equals 10, otherwise returns the incremented value. The function should not use a goto statement.
"""

def entrance(x):
    x += 1
    if x == 10:
        return entrance(x)
    return x