"""
QUESTION:
Write a function `get_permutations` that takes a string as input and returns a list of all unique permutations of the string. The function should ensure that each permutation is unique and the output list does not contain any duplicates. The input string may contain duplicate characters.
"""

def get_permutations(string):
    # Create a set to store unique permutations
    permutations = set()

    # Base case: if the string has only one character, return it as a single permutation
    if len(string) == 1:
        return [string]

    # For each character in the string
    for i, char in enumerate(string):
        # Get all permutations of the remaining characters
        remaining_chars = string[:i] + string[i+1:]
        for perm in get_permutations(remaining_chars):
            # Add the current character to the front of each permutation
            permutations.add(char + perm)

    # Convert the set to a list and return it
    return list(permutations)