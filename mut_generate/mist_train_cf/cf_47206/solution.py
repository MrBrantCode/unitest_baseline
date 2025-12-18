"""
QUESTION:
Write a function `find_min(tpl)` that takes a non-empty tuple `tpl` of integers as input and returns the smallest integer value in the tuple without using the built-in `min()` function or sorting the tuple.
"""

def find_min(tpl):
    min_value = tpl[0]  # We start from the first element
    for i in tpl:
        if i < min_value:
            min_value = i  # If we found a lesser value, we update our minimum
    return min_value