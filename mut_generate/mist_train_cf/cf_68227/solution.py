"""
QUESTION:
Write a function `generate_permutations(input_str)` that generates all permutations of the input string. The function should take a string of unique alphabetical characters as input and return a list of all possible permutations of the input string. The input string may contain multiple characters.
"""

def generate_permutations(input_str):
    if len(input_str) == 1:
        return [input_str]

    permutations = []
    for char in input_str:
        [permutations.append(char + p) for p in generate_permutations(input_str.replace(char, "", 1))]

    return permutations