"""
QUESTION:
Write a function `count_occurrences(string, character)` that takes two parameters: a string and a character. Without using any built-in string counting functions or methods, return the number of times the character appears in the string.
"""

def count_occurrences(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count