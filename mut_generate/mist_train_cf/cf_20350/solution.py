"""
QUESTION:
Create a function `count_unique_characters` that takes a string as input and returns the number of unique characters in the string, excluding characters that are surrounded by single or double quotation marks. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def count_unique_characters(string):
    unique_chars = set()
    in_quotes = False
    i = 0

    while i < len(string):
        if string[i] == '"' or string[i] == "'":
            # Toggle in_quotes flag when a quotation mark is encountered
            in_quotes = not in_quotes
            i += 1
        elif not in_quotes:
            # If not inside quotation marks, add character to unique_chars set
            unique_chars.add(string[i])
            i += 1
        else:
            # Skip characters inside quotation marks
            i += 1

    return len(unique_chars)