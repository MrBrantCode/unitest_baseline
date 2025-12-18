"""
QUESTION:
Create a function `unique_characters(strings)` that takes a list of strings as input and returns a string containing all unique characters from the input strings. The function should have a time complexity of O(N) and space complexity of O(N), where N is the total number of characters in all the strings combined.
"""

def unique_characters(strings):
    unique_chars = set()
    for string in strings:
        for char in string:
            unique_chars.add(char)
    return ''.join(unique_chars)