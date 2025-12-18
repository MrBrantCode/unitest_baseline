"""
QUESTION:
Write a function `capitalize_string` that takes a string as input and returns a new string where the first letter of each word is capitalized. The function should handle special characters and correctly capitalize the first letter after each special character. The function should have a time complexity of O(n) and should not use any built-in string manipulation functions.
"""

def capitalize_string(string):
    capitalized_string = ""
    should_capitalize_next = True

    for char in string:
        if should_capitalize_next and char.isalpha():
            capitalized_string += char.upper()
            should_capitalize_next = False
        else:
            capitalized_string += char
            if char in ['.', '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '<', '>', '\'', '\"']:
                should_capitalize_next = True
            elif char == ' ':
                should_capitalize_next = True

    return capitalized_string