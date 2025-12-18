"""
QUESTION:
Create a function `does_it_balance(p, t)` that takes a tuple `p` and a total capacity `t` as input. The function should return `True` if the sum of the elements in `p` does not exceed `t` and `p` is symmetric (i.e., the same items are on both ends), and `False` otherwise.
"""

def does_it_balance(p, t):
    if sum(p) > t: # Check if sum of numbers in tuple is within total capacity
        return False
    else: # Check if tuple is symmetric
        return p == p[::-1]  