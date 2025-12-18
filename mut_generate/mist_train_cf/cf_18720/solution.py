"""
QUESTION:
Write a function `generate_permutations(word)` that generates all permutations of the input word without using any built-in library functions for generating permutations. The function should have a time complexity of O(n!), where n is the length of the input word.
"""

def generate_permutations(word):
    if len(word) == 0:
        return [[]]

    permutations = []
    for i in range(len(word)):
        char = word[i]
        remaining_chars = word[:i] + word[i+1:]
        sub_permutations = generate_permutations(remaining_chars)

        for sub_permutation in sub_permutations:
            permutations.append([char] + sub_permutation)

    return permutations