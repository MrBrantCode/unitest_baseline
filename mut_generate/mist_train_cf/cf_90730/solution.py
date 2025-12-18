"""
QUESTION:
Create a function `remove_special_characters` that takes a string as input and returns a new string with all special characters removed. Special characters are defined as any non-alphanumeric characters. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in string manipulation functions such as `replace()` or `translate()`.
"""

def remove_special_characters(string):
    new_string = ""
    
    for char in string:
        if char.isalnum():
            new_string += char
    
    return new_string