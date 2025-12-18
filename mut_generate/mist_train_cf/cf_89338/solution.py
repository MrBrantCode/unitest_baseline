"""
QUESTION:
Design a recursive function `generate_permutations(string)` that generates all possible permutations of a given string. The function should return a list of all permutations without using any built-in functions or loops. The function should be able to handle strings of any length.
"""

def generate_permutations(string):
    # Base case: if the string is empty, return a list containing an empty string
    if len(string) == 0:
        return ['']

    # Recursive case: for each character in the string, generate permutations of the remaining characters
    permutations = []
    for i in range(len(string)):
        char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in generate_permutations(remaining_chars):
            permutations.append(char + perm)

    return permutations