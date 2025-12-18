"""
QUESTION:
Develop a function `allPermutations(str)` that generates all permutations of the input string `str`, handles duplicate characters, and identifies the palindrome permutations. The function should return two lists: one containing all permutations and another containing only the palindrome permutations.
"""

import itertools

def allPermutations(str):
    # Get all permutations of the string 'str'
    permutations = [''.join(p) for p in itertools.permutations(str)]
    
    # Instantiate a list to store palindrome permutations
    palindrome_permutations = []

    # Iterate over the permutations
    for permutation in permutations:
        # Use a slicing method to check if the string is a palindrome
        if permutation == permutation[::-1]:
            palindrome_permutations.append(permutation)
    
    # Return all permutations and palindrome permutations
    return permutations, palindrome_permutations