"""
QUESTION:
Write a function named `count_occurrences` that takes a string and a character as input, and returns the number of occurrences of the character in the string. The function should be case-insensitive and count occurrences of the character as part of a larger substring. It should handle strings with special characters and spaces.
"""

def count_occurrences(string, character):
    count = 0
    for char in string:
        if char.lower() == character.lower():
            count += 1
    return count