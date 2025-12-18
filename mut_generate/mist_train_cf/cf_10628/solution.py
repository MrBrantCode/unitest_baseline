"""
QUESTION:
Implement a function named `custom_length` that calculates the number of characters in a given string, including spaces and special characters. The function should handle edge cases such as empty strings and strings with leading or trailing spaces, and it should not use any built-in functions or methods that directly give the length of a string.
"""

def custom_length(string):
    count = 0
    for char in string:
        count += 1
    return count