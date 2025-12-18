"""
QUESTION:
Implement a function `custom_length(string)` that calculates the length of a given string, including spaces and special characters, without using built-in length functions or methods. The function should handle edge cases such as empty strings, leading/trailing spaces, consecutive spaces, Unicode characters, and non-ASCII characters.
"""

def custom_length(string):
    count = 0
    for char in string:
        count += 1
    return count