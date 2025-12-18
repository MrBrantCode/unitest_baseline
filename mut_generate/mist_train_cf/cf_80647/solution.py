"""
QUESTION:
Create a function `replace_special_symbols` that transforms each unique special symbol present in a string into its corresponding ASCII numerical equivalent. The function should handle a string containing alphanumeric characters and special characters. The special characters to be considered include `!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`.
"""

def replace_special_symbols(text):
    special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    result = ''
    for char in text:
        if char in special_characters:
            result += str(ord(char))
        else:
            result += char
    return result