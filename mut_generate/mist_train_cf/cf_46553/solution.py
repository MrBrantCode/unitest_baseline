"""
QUESTION:
Write a function called `powerset(s)` that generates all distinct subsets from a given string `s`, ignoring the order of characters and including the empty set and the set itself. The function should return these subsets as a list of strings.
"""

from itertools import chain, combinations

def powerset(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))