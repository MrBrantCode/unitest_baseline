"""
QUESTION:
Write a function `remove_char(string, char)` that removes all occurrences of a character `char` from a given string `string` and returns the resulting string. The function should be able to handle special characters and whitespaces. The function should not use any built-in string manipulation functions, loops, or recursion, and should have a time complexity of O(n), where n is the length of the string.
"""

def remove_char(string, char):
    new_string = ""
    for i in range(len(string)):
        if string[i] != char:
            new_string += string[i]
    return new_string