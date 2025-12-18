"""
QUESTION:
Create a function named `count_vowels` that takes a string as input and returns a dictionary containing the count of each vowel found in the string along with their positions. The function should consider both lowercase and uppercase vowels, ignore non-alphabet characters and spaces, and handle empty strings or strings with only non-alphabet characters and spaces by returning an empty dictionary.
"""

def count_vowels(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    vowel_positions = {}

    for i, char in enumerate(string):
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in vowels:
                vowels[char_lower] += 1
                if char_lower not in vowel_positions:
                    vowel_positions[char_lower] = []
                vowel_positions[char_lower].append(i)

    return vowel_positions if vowel_positions else {}