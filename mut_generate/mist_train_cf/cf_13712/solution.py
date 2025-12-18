"""
QUESTION:
Write a function named `hex_to_rgb` that takes a valid hexadecimal color code as a string and returns a string representing the RGB format of the color. The RGB format should be in the form "RGB(x, y, z)" where x, y, and z are integers representing the red, green, and blue components of the color respectively. Do not use any built-in functions or libraries.
"""

def hex_to_rgb(hex_code):
    # Convert each pair of characters to decimal values
    red = int(hex_code[1:3], 16)
    green = int(hex_code[3:5], 16)
    blue = int(hex_code[5:7], 16)
    
    # Format the result as "RGB(x, y, z)"
    result = "RGB({}, {}, {})".format(red, green, blue)
    return result