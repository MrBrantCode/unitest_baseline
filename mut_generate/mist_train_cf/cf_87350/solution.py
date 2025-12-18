"""
QUESTION:
Create a function `generate_strings(character_set, k)` that generates all possible strings of length `k` from a given character set. The `character_set` is a string of lowercase characters and `k` is the maximum length of the strings, where `k` is less than or equal to 15. The function should return a list of all possible strings of length `k` using the characters in the `character_set`.
"""

def generate_strings(character_set, k):
    if k <= 0:
        return []

    strings = []
    for char in character_set:
        if k == 1:
            strings.append(char)
        else:
            for string in generate_strings(character_set, k - 1):
                strings.append(char + string)

    return strings