"""
QUESTION:
Create a function called `convert_string` that takes a string as input, removes any non-alphabetic characters, replaces each alphabetic character with its corresponding ASCII code, removes duplicates while preserving the order of the remaining codes, reverses the resulting string of ASCII codes, and returns the final string. The function should treat uppercase and lowercase characters as separate entities.
"""

def convert_string(input_string):
    # Remove special characters and whitespace from input string
    input_string = ''.join(filter(str.isalpha, input_string))

    # Convert characters to ASCII codes and remove duplicates while preserving order
    ascii_codes = []
    [ascii_codes.append(str(ord(char))) for char in input_string if str(ord(char)) not in ascii_codes]

    # Reverse the resulting string
    reversed_string = ''.join(ascii_codes[::-1])

    return reversed_string