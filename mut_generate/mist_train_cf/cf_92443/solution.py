"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters: a string and a list of characters. The function should return the total count of occurrences of all characters in the string, ignoring case sensitivity.
"""

def count_occurrences(string, characters):
    count = 0
    for char in characters:
        count += string.lower().count(char.lower())
    return count