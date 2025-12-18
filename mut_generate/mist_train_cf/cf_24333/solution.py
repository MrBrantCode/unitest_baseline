"""
QUESTION:
Create a function called `generate_combinations` that returns an array of strings containing all possible combinations of n characters from a given string of characters, allowing repetitions. The function should take two parameters: `characters` (a string of characters) and `n` (the number of characters in each combination).
"""

import itertools

def generate_combinations(characters, n):
    """
    Returns an array of strings containing all possible combinations of n characters from a given string of characters, allowing repetitions.

    Args:
        characters (str): A string of characters.
        n (int): The number of characters in each combination.

    Returns:
        list: A list of strings containing all possible combinations.
    """
    return [''.join(p) for p in itertools.product(characters, repeat=n)]