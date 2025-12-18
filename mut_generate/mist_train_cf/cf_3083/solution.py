"""
QUESTION:
Write a function named `remove_duplicates` that takes a string as input, removes duplicate characters, sorts the unique characters in descending order based on their ASCII values, and returns the resulting string. The function should not use any external libraries or built-in sorting functions that take more than one argument.
"""

def remove_duplicates(s):
    unique_chars = list(set(s))
    unique_chars.sort(reverse=True, key=lambda x: ord(x))
    result = ""
    for char in unique_chars:
        result += char
    return result