"""
QUESTION:
Write a function `generate_permutations(word)` that generates all permutations of a given word without using any built-in library functions for generating permutations. The function should take a string as input and return a list of all possible permutations of the input string.
"""

def generate_permutations(word):
    if len(word) == 1:
        return [word]

    permutations = []
    for i in range(len(word)):
        for perm in generate_permutations(word[:i] + word[i+1:]):
            permutations.append(word[i] + perm)
    
    return permutations