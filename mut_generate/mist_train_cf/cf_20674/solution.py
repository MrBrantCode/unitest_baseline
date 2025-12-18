"""
QUESTION:
Create a function `replace_letters_with_ascii` that takes a string as input and replaces all occurrences of the letters 'H', 'W', 'o', 'l', and 'd' (case-insensitive) with their corresponding ASCII values, while maintaining the original case of the replaced letters. If the input string is empty or no letters are replaced, print an appropriate message. The function should handle non-English characters and use efficient algorithms.
"""

def replace_letters_with_ascii(input_string):
    if not input_string:
        print("Input string is empty.")
        return

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

    if modified_string == input_string:
        print("No letters to replace.")
    else:
        print(modified_string)