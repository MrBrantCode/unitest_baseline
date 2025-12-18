"""
QUESTION:
Create a function `ascii_conversion` that takes a list of uppercase alphabetical characters as input and returns a dictionary. The dictionary should map each character to another dictionary containing its corresponding hexadecimal and ASCII values. Use the built-in `ord` function to convert characters to their ASCII values and `hex` function to convert integers to hexadecimal strings. The function should handle multiple characters and return the results in the specified format.
"""

def ascii_conversion(letters):
    result = {}
    for letter in letters:
        ascii_val = ord(letter)
        hex_val = hex(ascii_val)
        result[letter] = {'Hexadecimal': hex_val, 'ASCII': ascii_val}
    return result