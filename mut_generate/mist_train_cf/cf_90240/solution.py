"""
QUESTION:
Write a function called `remove_spaces` that takes a string of text as input, removes all white spaces, and converts all characters to lowercase without using built-in functions for case conversion. The output should maintain the original order of characters.
"""

def remove_spaces(text):
    text = ''.join(text.split())
    return ''.join([chr(ord(char) + 32) if ord('A') <= ord(char) <= ord('Z') else char for char in text])