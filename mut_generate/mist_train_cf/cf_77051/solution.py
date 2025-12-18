"""
QUESTION:
Write a function `rgb_to_hex_and_complementary` that takes a tuple of three integers in the range 0-255 representing an RGB color and returns a tuple containing two strings: the HEX value of the input RGB color and the HEX value of its closest complementary color.
"""

def rgb_to_hex_and_complementary(rgb):
    # Convert RGB to HEX
    rgb_hex = '#{:02X}{:02X}{:02X}'.format(*rgb)
    
    # Find the complementary color
    complementary_rgb = tuple(255 - i for i in rgb)
    
    # Convert the complementary color to HEX
    complementary_hex = '#{:02X}{:02X}{:02X}'.format(*complementary_rgb)
    
    return rgb_hex, complementary_hex