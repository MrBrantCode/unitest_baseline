"""
QUESTION:
Create a function called `generate_strings` that takes a set of lowercase characters and an integer `k` as input, where `k` is the length of the strings to be generated and is less than or equal to 15. The function should return all possible strings of length `k` that can be formed using the characters in the given set.
"""

def generate_strings(character_set, k):
    if k == 0:
        return ['']
    
    strings = []
    for char in character_set:
        for string in generate_strings(character_set, k-1):
            strings.append(char + string)
    
    return strings