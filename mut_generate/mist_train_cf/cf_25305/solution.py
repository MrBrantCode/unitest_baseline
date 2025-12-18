"""
QUESTION:
Write a function called `permutate` that generates all possible permutations of a given string. The function should take a string as input and return a list of strings, each representing a unique permutation of the input string.
"""

def permutate(s):
    """
    Generates all possible permutations of a given string.

    Args:
        s (str): The input string.

    Returns:
        list: A list of strings, each representing a unique permutation of the input string.
    """
    if len(s) <= 1:
        return [s]
    permutations = []
    for i in range(len(s)):
        char = s[i]
        remaining_string = s[:i] + s[i+1:]
        for sub_permutation in permutate(remaining_string):
            permutations.append(char + sub_permutation)
    return permutations