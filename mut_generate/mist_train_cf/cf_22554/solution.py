"""
QUESTION:
Write a function called `remove_white_spaces` that takes a string as input and returns a new string where all white spaces have been removed and all characters are in lowercase. The function should iterate through the input string only once, achieving a time complexity of O(n), where n is the length of the input string. Do not use built-in string manipulation functions or regular expressions.
"""

def remove_white_spaces(string):
    output = ""
    for char in string:
        if char != " ":
            output += char.lower()
    return output