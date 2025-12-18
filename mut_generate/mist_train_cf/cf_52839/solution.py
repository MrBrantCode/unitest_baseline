"""
QUESTION:
Generate all unique combinations of a given string and filter out combinations that do not contain vowels. The function should be named `filter_vowels` and it should return a list of combinations in alphabetical order. The vowels to be considered are 'a'. The input string is "abcd".
"""

import itertools

def filter_vowels(input_str):
    # Generate all unique combinations
    combinations = ["".join(comb) for i in range(1, len(input_str) + 1) for comb in itertools.combinations(sorted(input_str), i)]

    # Filter out combinations that do not have vowels
    return sorted([comb for comb in combinations if any(vowel in comb for vowel in 'a')])