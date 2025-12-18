"""
QUESTION:
Write a function `count_occurrences` that takes a string and a list of characters as input and returns the total count of all the characters in the string, ignoring case sensitivity. The function should be able to handle strings with a length of up to 1 million characters.
"""

def count_occurrences(string, characters):
    count = 0
    string = string.lower()
    for char in characters:
        count += string.count(char.lower())
    return count