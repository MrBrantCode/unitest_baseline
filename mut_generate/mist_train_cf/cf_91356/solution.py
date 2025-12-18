"""
QUESTION:
Create a function `generate_strings(character_set, k)` that generates all possible strings of length `k` using the characters in `character_set`. The function should take two parameters: `character_set`, a set of lowercase characters, and `k`, an integer representing the length of the strings to generate, where `k` is less than or equal to 10.
"""

def generate_strings(character_set, k):
    """
    Generates all possible strings of length k using the characters in character_set.

    Args:
    character_set (set): A set of lowercase characters.
    k (int): The length of the strings to generate.

    Returns:
    list: A list of all possible strings of length k.
    """
    strings = []
    if k == 0:
        return ['']
    for char in character_set:
        for string in generate_strings(character_set, k-1):
            strings.append(char + string)
    return strings