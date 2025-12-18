"""
QUESTION:
Write a function named `convert_hex_to_rgb` that takes a string `hex_code` as input, representing a 6-digit hexadecimal color code without any leading "#" symbol. The function should convert the hexadecimal color code to RGB format and return a string in the format "RGB(x, y, z)" where x, y, and z are integers representing the red, green, and blue components of the color respectively, in the range 0-255. If the input color code is not valid (i.e., it does not consist of exactly 6 hexadecimal digits), the function should return an error message instead. The function should not use any built-in functions or libraries for converting the hexadecimal color code to RGB format.
"""

def convert_hex_to_rgb(hex_code):
    # Validate the input hexadecimal color code
    if len(hex_code) != 6 or not all(c.isdigit() or c.lower() in 'abcdef' for c in hex_code):
        return 'Invalid hexadecimal color code'

    # Convert the hexadecimal color code to RGB format
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    rgb_format = f"RGB({r}, {g}, {b})"
    return rgb_format