"""
QUESTION:
Analyze the time complexity of a recursive function called `recursive_function` that takes a positive integer `n` as input, with the function implemented such that it makes recursive calls until `n` reaches 0. The function should not perform any additional work beyond the recursive calls and the base case check.
"""

def entrance(n):
    if n == 0:
        return
    else:
        entrance(n-1)