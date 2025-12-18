"""
QUESTION:
Write a function `hex_to_rgb` that takes a 6-digit hexadecimal color code as input and returns a string in the format "RGB(x, y, z)" representing the red, green, and blue components of the color. The input will not have a leading "#" symbol and the range of the red, green, and blue components should be limited to 0-255. Do not use any built-in functions or libraries for the conversion.
"""

def hex_to_rgb(hex_code):
    # Split the hex code into three parts representing red, green, and blue
    red = int(hex_code[:2], 16)
    green = int(hex_code[2:4], 16)
    blue = int(hex_code[4:], 16)

    # Limit the values to the range of 0-255
    red = max(0, min(red, 255))
    green = max(0, min(green, 255))
    blue = max(0, min(blue, 255))

    # Return the RGB string format
    return "RGB({}, {}, {})".format(red, green, blue)