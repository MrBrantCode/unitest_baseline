"""
QUESTION:
Create a function called `replace_repeating_chars` that takes a string as input and returns the modified string with consecutive repeating characters replaced, while retaining the original character casing. The function should handle both uppercase and lowercase characters.
"""

def replace_repeating_chars(input_string: str) -> str:
    modified_string = ""
    prev_char = ""
    for char in input_string:
        if char.lower() != prev_char.lower():
            modified_string += char
        prev_char = char
    return modified_string