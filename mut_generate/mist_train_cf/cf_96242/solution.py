"""
QUESTION:
Write a function `replace_letters_with_ascii` that takes a string as input and replaces all occurrences of the letters 'H', 'W', 'o', 'l', and 'd' (case-insensitive) with their corresponding ASCII values while maintaining the original case of the replaced letters. The function should handle edge cases, such as an empty input string or no occurrences of the letters to be replaced, and ignore non-English characters.
"""

def replace_letters_with_ascii(input_string):
    ascii_replacements = {
        'H': '72',
        'W': '87',
        'o': '111',
        'l': '108',
        'd': '100'
    }

    modified_string = ""
    for char in input_string:
        if char.upper() in ascii_replacements:
            modified_string += ascii_replacements[char.upper()]
        else:
            modified_string += char

    return modified_string