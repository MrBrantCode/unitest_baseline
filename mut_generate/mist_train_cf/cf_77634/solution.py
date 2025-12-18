"""
QUESTION:
Write a function `remove_duplicate_characters` that takes a string as an argument, removes all the duplicate characters from it, and returns the modified string with the first occurrences of the characters in the order of appearance. The function should not use any built-in string or list methods other than indexing and concatenation.
"""

def remove_duplicate_characters(string):
    result = ""
    for char in string:
        if char not in result:
            result += char
    return result