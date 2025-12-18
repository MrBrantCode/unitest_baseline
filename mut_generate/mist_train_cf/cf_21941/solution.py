"""
QUESTION:
Write a function `generate_permutations(string)` to generate all possible permutations of a given string. The input string contains only lowercase alphabets and may contain duplicate characters. The length of the input string does not exceed 10. The output list should be sorted in lexicographically increasing order. The solution should have a time complexity of O(n!) or better, where n is the length of the input string, and should not use recursion.
"""

from itertools import permutations

def generate_permutations(string):
    # Convert the string into a list of characters
    chars = list(string)
    
    # Generate all possible permutations of the characters
    perms = permutations(chars)
    
    # Convert each permutation tuple back into a string
    perm_strings = [''.join(perm) for perm in perms]
    
    # Sort the list of permutation strings in lexicographically increasing order
    perm_strings.sort()
    
    return perm_strings