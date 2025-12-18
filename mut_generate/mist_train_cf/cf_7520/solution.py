"""
QUESTION:
Create a function called "toggle_string" that takes a string as input, toggles each character's case, and returns the toggled string. Then, count the number of times each character appears in the toggled string and return the count as a dictionary. The input string is "Hello World!". The function should handle non-alphabet characters.
"""

def toggle_string(s):
    toggled_string = ""
    char_count = {}
    for char in s:
        if char.isalpha():
            toggled_string += char.swapcase()
        else:
            toggled_string += char
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return toggled_string, char_count