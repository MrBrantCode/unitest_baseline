"""
QUESTION:
Create a function called rgb_to_hex that takes three integers (red, green, blue) ranging from 0 to 255, converts each decimal value to its hexadecimal representation (padding with a zero if necessary), and returns the concatenated hexadecimal values as a string prefixed with '#'.
"""

def rgb(r, g, b):
    # Convert each RGB component to hexadecimal
    red_hex = format(r, '02x')
    green_hex = format(g, '02x')
    blue_hex = format(b, '02x')

    # Concatenate the hexadecimal values together
    hex_color = "#" + red_hex + green_hex + blue_hex

    return hex_color