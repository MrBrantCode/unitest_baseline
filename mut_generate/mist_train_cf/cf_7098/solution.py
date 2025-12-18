"""
QUESTION:
Write a function `remove_vowels` that takes a string as input and returns a new string with all lowercase vowels (a, e, i, o, u) removed, leaving all other characters unchanged. The function should be case-sensitive, not removing uppercase vowels.
"""

def remove_vowels(string):
    vowels = 'aeiou'
    new_string = ''
    for char in string:
        if char.lower() not in vowels:
            new_string += char
    return new_string