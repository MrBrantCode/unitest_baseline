"""
QUESTION:
Write a function `get_permutations` that generates all possible permutations of the input string without using any built-in permutation functions. The input string can contain duplicate characters and special characters. The function should exclude duplicate permutations from the result.
"""

def get_permutations(string):
    # Base case: if the string is empty, return an empty list
    if len(string) == 0:
        return []

    # Base case: if the string contains only one character, return a list with the string itself
    if len(string) == 1:
        return [string]

    # Initialize an empty list to store the permutations
    permutations = []

    # Iterate through each character in the string
    for i in range(len(string)):
        # Extract the current character
        current_char = string[i]

        # Exclude duplicate characters to avoid duplicate permutations
        if string.index(current_char) != i:
            continue

        # Generate all permutations of the remaining characters
        remaining_chars = string[:i] + string[i+1:]
        for sub_permutation in get_permutations(remaining_chars):
            # Append the current character to each permutation of the remaining characters
            permutations.append(current_char + sub_permutation)

    return permutations