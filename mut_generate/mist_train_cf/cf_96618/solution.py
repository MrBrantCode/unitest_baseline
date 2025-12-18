"""
QUESTION:
Write a function `hex_to_rgb(hex_code)` that takes a 6-digit hexadecimal color code (without the "#" symbol) as input and returns a string representing the equivalent RGB color in the format "RGB(x, y, z)" where x, y, and z are integers between 0 and 255 representing the red, green, and blue components of the color respectively.
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