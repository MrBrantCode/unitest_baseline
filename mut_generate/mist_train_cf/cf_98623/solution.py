"""
QUESTION:
Implement a Python function called "vowel_trio" that takes a list of strings as input and returns a new list containing only the strings that start with the third vowel after 'y' in the English alphabet, considering only lowercase vowels as valid candidates.
"""

def vowel_trio(strings):
    vowels = ["a", "e", "i", "o", "u"]
    new_strings = []
    for string in strings:
        if string[0].lower() == 'i':
            new_strings.append(string)
    return new_strings