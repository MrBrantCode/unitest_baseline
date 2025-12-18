"""
QUESTION:
Generate all unique permutations of a given string. 

Implement a function named 'permutations' that takes a string as input and returns a set of strings, each representing a unique permutation of the input string. The function should handle strings of any length, including empty strings and strings with duplicate characters.
"""

def permutations(string):
    if len(string) <= 1:
        return set([string])

    last_char = string[-1]
    all_permutations = permutations(string[:-1])

    permutations_with_last_char = set()
    for permutation in all_permutations:
        for idx in range(len(string)):
            permutation_with_last_char = permutation[:idx] + last_char + permutation[idx:]
            permutations_with_last_char.add(permutation_with_last_char)

    return permutations_with_last_char