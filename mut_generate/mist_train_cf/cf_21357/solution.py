"""
QUESTION:
Create a function named `capitalize_string` that takes a string of any length as input and returns its capitalized version. The function should capitalize the first letter of each word and handle special characters by correctly capitalizing the first letter after each special character. The time complexity of the function should be O(n) and it should not use any built-in string manipulation functions.
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