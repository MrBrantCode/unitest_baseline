"""
QUESTION:
Write a function named `remove_character` that takes two parameters: `input_string` and `character_to_remove`. The function should remove all occurrences of `character_to_remove` from `input_string` and return the resulting string. The order of the remaining characters should be maintained. The function should not use any built-in string manipulation functions or libraries, and it should be able to handle input strings of up to 10^6 characters. The input string can contain both lowercase and uppercase letters, and the character to be removed can be either lowercase or uppercase.
"""

def remove_character(input_string, character_to_remove):
    new_string = ""
    for char in input_string:
        if char != character_to_remove:
            new_string += char
    return new_string