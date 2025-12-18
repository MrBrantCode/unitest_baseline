"""
QUESTION:
Generate a function `get_palindromic_permutations(s)` that returns all unique palindromic permutations of a given input string `s`. The function should be case-sensitive and consider the input string as a sequence of characters. Note that the function may not be efficient for very long strings due to the large number of permutations (n factorial, where n is the string length).
"""

from itertools import permutations

def get_palindromic_permutations(s):
    """Generate all palindrome permutations of a string"""
    perms = set(''.join(p) for p in permutations(s)) # use set to remove duplicates
    return [word for word in perms if word == word[::-1]] # check for palindrome