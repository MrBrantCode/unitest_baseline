"""
QUESTION:
Write a function `count_occurrences` that takes a string and a list of characters as input. The function should count the total occurrences of all characters in the string, ignoring case sensitivity. The input string can have a length of up to 1 million characters.
"""

def count_occurrences(string, characters):
    count = 0
    string = string.lower()
    for char in characters:
        count += string.count(char.lower())
    return count