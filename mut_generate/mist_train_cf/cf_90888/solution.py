"""
QUESTION:
Write a function `get_permutations(string)` that generates all unique permutations of a given string, even if it contains duplicate characters, and returns them as a list of strings.
"""

from itertools import permutations

def get_permutations(string):
    # Convert the string into a list of characters
    chars = list(string)
    
    # Use the permutations function from the itertools module to generate all possible permutations
    perms = permutations(chars)
    
    # Convert each permutation back into a string and add it to a list
    result = [''.join(perm) for perm in perms]
    
    # Remove any duplicate permutations by converting the list into a set and then back into a list
    result = list(set(result))
    
    return result