"""
QUESTION:
Trim a specified amount of characters from the beginning of a string while preserving the original string. The function should handle edge cases, such as when the specified amount is less than 0 or greater than or equal to the length of the string. Implement this in a function called `trim_string` that takes two parameters: the input string and the amount of characters to trim.
"""

def trim_string(string, amount):
    if amount >= 0 and amount < len(string):
        return string[amount:]
    else:
        return string