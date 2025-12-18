"""
QUESTION:
Create a function `lookup_rgb(rgb, color_dict)` that takes a dictionary `color_dict` where keys are unique hex color codes and values are their corresponding RGB tuples, and a RGB tuple `rgb` as input. The function should return the hex color code if the given RGB tuple exists in the dictionary values, otherwise return a message indicating the RGB value does not exist in the dictionary. The RGB tuples are of the form `(r, g, b)` where `r`, `g`, and `b` are decimal numbers ranging from 0.1 to 1.0.
"""

def lookup_rgb(rgb, color_dict):
    for hex_code, rgb_value in color_dict.items():
        if rgb_value == rgb:
            return hex_code
    return "This RGB value does not exist in the dictionary."