"""
QUESTION:
Write a recursive function `increment(x)` that increments the input number `x` by 1 until it reaches 10. The function should return the final value of `x`.
"""

def increment(x):
    x += 1
    if x < 10:
        return increment(x)
    return x