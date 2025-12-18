"""
QUESTION:
Write a function named `convert_string` that takes a string as input, removes non-alphabetic characters, converts each remaining character to its ASCII code, removes duplicates while preserving order of first occurrences, reverses the order of the resulting ASCII codes, and returns them as a string. The function should handle uppercase and lowercase letters as distinct entities.
"""

def convert_string(input_string):
    # Remove special characters and whitespace from input string
    input_string = ''.join(filter(str.isalpha, input_string))

    # Convert characters to ASCII codes and remove duplicates while preserving order
    seen = set()
    ascii_codes = [str(ord(char)) for char in input_string if not (char in seen or seen.add(char))]

    # Reverse the resulting string
    reversed_string = ''.join(ascii_codes[::-1])

    return reversed_string