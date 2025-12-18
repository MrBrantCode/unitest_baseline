"""
QUESTION:
Design a recursive function `generate_permutations` that takes a string as input and returns a list of all possible permutations of that string without using any built-in functions or loops. The function should only use recursive calls to generate the permutations.
"""

def generate_permutations(string):
    # Base case: if the string is empty, return an empty list
    if len(string) == 0:
        return []

    # Base case: if the string has only one character, return a list with that character
    if len(string) == 1:
        return [string]

    # Recursive case: for each character in the string, generate permutations of the remaining characters
    permutations = []
    for i in range(len(string)):
        char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in generate_permutations(remaining_chars):
            permutations.append(char + perm)

    return permutations