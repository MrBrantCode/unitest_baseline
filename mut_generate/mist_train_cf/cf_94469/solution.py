"""
QUESTION:
Create a function called rgb_to_hex that takes three parameters: r, g, b. The function should convert the given RGB value into a HEX color code. The RGB value consists of three integers ranging from 0 to 255. If any of the RGB components are invalid (less than 0 or greater than 255), the function should return "Invalid RGB value". The function should handle decimal RGB values by rounding them to the nearest integer and hexadecimal RGB values by converting them to decimal before performing the necessary calculations. The function should return the HEX color code as a string.
"""

def rgb_to_hex(r, g, b):
    # Check if any of the components is invalid
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        return "Invalid RGB value"

    # Convert decimal RGB values to hexadecimal
    r_hex = hex(round(r))[2:].zfill(2)
    g_hex = hex(round(g))[2:].zfill(2)
    b_hex = hex(round(b))[2:].zfill(2)

    # Concatenate the hexadecimal values
    hex_color = "#" + r_hex + g_hex + b_hex

    return hex_color