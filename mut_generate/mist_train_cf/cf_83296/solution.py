"""
QUESTION:
Write a function `buddyStrings(a, b)` that determines if it's possible to swap any two characters in string `a` such that it becomes identical to string `b`. The function should return `True` if it's feasible, and `False` otherwise. The input strings `a` and `b` are composed of lowercase letters and have a length between 1 and 2*10^4.
"""

def buddyStrings(a, b):
    if len(a) != len(b): return False
    if a == b and len(set(a)) < len(a): return True
    diff = [(c1, c2) for c1, c2 in zip(a, b) if c1 != c2]
    return len(diff) == 2 and diff[0] == diff[1][::-1]