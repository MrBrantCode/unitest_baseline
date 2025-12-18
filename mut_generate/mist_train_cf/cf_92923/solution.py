"""
QUESTION:
Convert a valid hexadecimal color code to an RGB string without using built-in functions or libraries. The output should be in the format "RGB(x, y, z)" where x, y, and z are integers representing the red, green, and blue components of the color.
"""

def hex_to_rgb(hex_code):
    # Convert each pair of characters to decimal values
    red = int(hex_code[1:3], 16)
    green = int(hex_code[3:5], 16)
    blue = int(hex_code[5:7], 16)
    
    # Format the result as "RGB(x, y, z)"
    result = "RGB({}, {}, {})".format(red, green, blue)
    return result