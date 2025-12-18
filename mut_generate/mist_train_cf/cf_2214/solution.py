"""
QUESTION:
Create a function called `generate_strings` that takes two parameters: `character_set` and `k`. The `character_set` parameter is a string of lowercase characters, and the `k` parameter is an integer representing the maximum length of the strings, which should be less than or equal to 15. The function should return a list of all possible strings of length `k` that can be generated using the characters in `character_set`.
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