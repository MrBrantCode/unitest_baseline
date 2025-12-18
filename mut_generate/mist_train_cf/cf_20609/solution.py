"""
QUESTION:
Write a function `get_rgb_value` that takes a dictionary of colors and a color name as input. The dictionary contains color names as keys and nested dictionaries as values, with the nested dictionaries containing a key "RGB" with RGB values as its value. The function should return the RGB value of the given color from the dictionary. If the color does not exist in the dictionary, the function should return a default RGB value of (0, 0, 0).
"""

def get_rgb_value(color_dict, color):
    if color in color_dict:
        return color_dict[color]["RGB"]
    else:
        return (0, 0, 0)