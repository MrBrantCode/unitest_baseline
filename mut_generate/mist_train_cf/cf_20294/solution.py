"""
QUESTION:
Implement a function named `remove_duplicates` that takes a string as an argument and returns a modified string where all duplicate characters are removed, regardless of their adjacency, while maintaining the order of the remaining characters. The function should be case-insensitive, treating uppercase and lowercase characters as duplicates.
"""

def remove_duplicates(string):
    unique_chars = set()
    new_string = ""

    for char in string:
        if char.lower() not in unique_chars:
            unique_chars.add(char.lower())
            new_string += char

    return new_string