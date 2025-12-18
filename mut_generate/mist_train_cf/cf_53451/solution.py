"""
QUESTION:
Implement a function named `decode_colors` that accepts a string of space-separated hex color codes and returns a list of RGB tuples. Each hex code is in the format '#fff', where each character represents a decimal value multiplied by 17. The function should interpret each hex code and return a corresponding RGB tuple. 

The hex code '#fff' should be translated to the RGB tuple (255, 255, 255), '#000' to (0, 0, 0), and '#f00' to (255, 0, 0).
"""

from typing import List, Tuple

def decode_colors(color_string: str) -> List[Tuple[int, int, int]]:
    hex_to_dec_map = {
        '0': 0,
        '1': 17,
        '2': 34,
        '3': 51,
        '4': 68,
        '5': 85,
        '6': 102,
        '7': 119,
        '8': 136,
        '9': 153,
        'a': 170,
        'b': 187,
        'c': 204,
        'd': 221,
        'e': 238,
        'f': 255
    }
    
    color_strings = color_string.split()
    rgb_tuples = []
    
    for color in color_strings:
        r_val = hex_to_dec_map[color[1]]
        g_val = hex_to_dec_map[color[2]]
        b_val = hex_to_dec_map[color[3]]
        rgb_tuples.append((r_val, g_val, b_val))
        
    return rgb_tuples