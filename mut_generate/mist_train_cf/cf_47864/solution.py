"""
QUESTION:
Write a function `word_permutations` that takes a list of lower-case words as input and returns a list of all unique permutations of these words, with each permutation in reverse order and upper case. If the input list is empty, return an empty list. The order of individual letters within words should be preserved.
"""

from itertools import permutations

def word_permutations(word_list):
    if not word_list:
        return []

    unique_permutes = []
    for permute in permutations(word_list, len(word_list)):
        reverse_upper = [word.upper() for word in permute[::-1]]
        unique_permutes.append(reverse_upper)
        
    return unique_permutes