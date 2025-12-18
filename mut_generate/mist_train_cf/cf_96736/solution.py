"""
QUESTION:
Create a function called `remove_vowels` that takes a string as an argument and returns the string with all vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') removed. The input string can contain both uppercase and lowercase letters.
"""

def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string