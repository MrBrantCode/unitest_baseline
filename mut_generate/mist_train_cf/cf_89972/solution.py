"""
QUESTION:
Create a function called "toggle_string" that takes a string as input and returns the string with all characters toggled to their opposite case. The function should also count the number of times each character appears in the toggled string. The function should return both the toggled string and a dictionary with the character counts. 

The function should work with any string and should handle both alphabetic and non-alphabetic characters. Non-alphabetic characters should be included in the count dictionary. The function should not modify the original string. 

For example, given the string "Hello World!", the function should return the string "hELLO wORLD!" and a dictionary with the count of each character in the toggled string.
"""

def toggle_string(string):
    toggled_string = ""
    character_count = {}
    for char in string:
        if char.isalpha():
            toggled_string += char.swapcase()
        else:
            toggled_string += char
        if char.swapcase() in character_count:
            character_count[char.swapcase()] += 1
        else:
            character_count[char.swapcase()] = 1
    return toggled_string, character_count