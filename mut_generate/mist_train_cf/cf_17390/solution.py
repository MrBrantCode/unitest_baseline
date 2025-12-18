"""
QUESTION:
Implement a function named `custom_length` that calculates the length of a given string. The function should manually count the number of characters in the string, including spaces and special characters, without using any built-in string length functions. The function should handle edge cases such as empty strings, strings with leading or trailing spaces, consecutive spaces, Unicode characters, and non-ASCII characters.
"""

def custom_length(string):
    count = 0
    for char in string:
        count += 1
    return count