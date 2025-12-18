"""
QUESTION:
Write a function named `convert_hex_to_rgb` that takes a 6-digit hexadecimal color code as a string without any leading "#" symbol and returns a string representing the color in RGB format "RGB(x, y, z)" where x, y, and z are integers between 0-255 representing the red, green, and blue components of the color respectively. The function should validate the input hexadecimal color code and return an error message if the code is not valid, i.e., it does not consist of exactly 6 characters or contains characters other than hexadecimal digits (0-9, A-F or a-f).
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