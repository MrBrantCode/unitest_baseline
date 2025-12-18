"""
QUESTION:
Create a function `generate_strings` that generates all possible strings of a given length `k` from a set of lowercase characters `character_set`. The function should take two parameters: `character_set` and `k`, where `k` is the maximum length of the strings and is less than or equal to 10.
"""

def generate_strings(character_set, k):
    strings = []
    if k == 0:
        return ['']
    for char in character_set:
        for string in generate_strings(character_set, k-1):
            strings.append(char + string)
    return strings