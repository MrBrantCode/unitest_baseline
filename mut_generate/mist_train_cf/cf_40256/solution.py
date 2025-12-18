"""
QUESTION:
Write a function called `feast` that takes two non-empty strings as input: `beast` and `dish`. The function should return `True` if the first and last characters of `beast` are the same as the first and last characters of `dish`, respectively, and `False` otherwise. The comparison should be case-sensitive.
"""

def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]