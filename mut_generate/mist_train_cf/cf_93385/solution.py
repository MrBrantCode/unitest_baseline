"""
QUESTION:
Create a function `count_characters` that takes a list of strings as an argument and returns the total number of alphabetic characters in all the strings combined, excluding any non-alphabetic characters including special characters and white spaces.
"""

def count_characters(strings):
    total_characters = 0
    for string in strings:
        for char in string:
            if char.isalpha():
                total_characters += 1
    return total_characters