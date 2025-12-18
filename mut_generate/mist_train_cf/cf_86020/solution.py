"""
QUESTION:
Write a function named `generate_combinations` that takes two parameters: a string `characters` and an integer `length`. The function should return an array of all possible combinations of the characters in the string, with each combination having the specified length. The combinations should include repetitions of characters.
"""

import itertools

def generate_combinations(characters, length):
    combinations = [''.join(p) for p in itertools.product(characters, repeat=length)]
    return combinations