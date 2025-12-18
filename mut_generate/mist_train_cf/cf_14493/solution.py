"""
QUESTION:
Write a function `reformat_condition` that takes no arguments and returns a reformatted if statement with only one condition, given the original condition is `(x < 0 and y >= 0) or (x >= 0 and y < 0)`. The reformatted condition should be logically equivalent to the original condition.
"""

def reformat_condition(x, y):
    return (x < 0 and y >= 0) or (x >= 0 and y < 0)