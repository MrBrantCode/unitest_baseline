"""
QUESTION:
Write a function named `print_permutations` that prints all possible permutations of a given string, including repeated characters. The function should take a string as input and print each permutation of the string.
"""

def print_permutations(s):
    if len(s) == 0:
        return [s]
    permutations = []
    for i in range(len(s)):
        character = s[i]
        remaining_characters = s[:i] + s[i+1:]
        sub_permutations = print_permutations(remaining_characters)
        for sub_permutation in sub_permutations:
            permutations.append(character + sub_permutation)
    return permutations