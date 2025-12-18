"""
QUESTION:
Write a function `string_to_list(string)` that converts a given string to a list of characters, excluding any whitespace characters. The function must achieve this in O(n) time complexity without using built-in string or list methods (e.g., str.split(), list(), or str.join()), regular expressions, or third-party libraries. The function should correctly handle strings with leading or trailing whitespace characters.
"""

def string_to_list(string):
    string = string.strip()
    char_list = []
    for char in string:
        if char != ' ':
            char_list.append(char)
    return char_list