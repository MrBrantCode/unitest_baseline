"""
QUESTION:
Write a function named `convert_to_camel_case` that takes a string as input and returns the string converted to CamelCase. The function should handle strings of any length, leading and trailing spaces, multiple consecutive spaces, special characters, and numbers. It should not use any built-in functions or libraries to convert the string to CamelCase. The function should have an efficient runtime complexity.
"""

def convert_to_camel_case(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Initialize the result string
    result = ''

    # Initialize a flag to indicate if the current character should be capitalized
    capitalize_next = False

    # Iterate through each character in the string
    for char in string:
        # If the character is a space, set the flag to capitalize the next character
        if char == ' ':
            capitalize_next = True
        # If the character should be capitalized, append it to the result string in uppercase
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        # If the character should not be capitalized, append it to the result string as is
        else:
            result += char

    # Capitalize the first character if it is a letter
    if result and result[0].isalpha():
        result = result[0].upper() + result[1:]

    return result