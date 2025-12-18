"""
QUESTION:
Write a function `remove_vowels(string)` that takes a string as input and returns a new string with all vowels removed. The function should consider both lowercase and uppercase vowels.
"""

def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string