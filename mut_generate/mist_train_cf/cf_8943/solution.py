"""
QUESTION:
Create a function named `count_vowels` that takes a string as input and returns a dictionary with two keys: 'count' and 'positions'. The 'count' key should map each vowel ('a', 'e', 'i', 'o', 'u') to its frequency in the string, ignoring case, non-alphabet characters, and spaces. The 'positions' key should map each vowel to a list of its indices in the string.
"""

def count_vowels(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    vowels_positions = {'a': [], 'e': [], 'i': [], 'o': [], 'u': []}

    for i, char in enumerate(string):
        if char.lower() in vowels:
            vowels[char.lower()] += 1
            vowels_positions[char.lower()].append(i)

    return {'count': vowels, 'positions': vowels_positions}