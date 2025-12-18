"""
QUESTION:
Create a function called `count_vowels` that takes a string as input and returns a dictionary with two keys: 'count' and 'positions'. The 'count' key should contain a dictionary with the count of each vowel ('a', 'e', 'i', 'o', 'u') found in the string, considering both uppercase and lowercase letters and ignoring non-alphabet characters and spaces. The 'positions' key should contain a dictionary with a list of positions for each vowel found. The function should handle strings with any combination of uppercase and lowercase letters, spaces, and non-alphabet characters.
"""

def count_vowels(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    vowels_positions = {'a': [], 'e': [], 'i': [], 'o': [], 'u': []}

    for i, char in enumerate(string):
        if char.lower() in vowels:
            vowels[char.lower()] += 1
            vowels_positions[char.lower()].append(i)

    return {'count': vowels, 'positions': vowels_positions}