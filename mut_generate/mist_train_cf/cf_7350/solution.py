"""
QUESTION:
Write a function `validate_font_size` that takes a string font size as input, and returns True if the font size is a valid integer between 10 and 40, False otherwise. 

Write another function `validate_font_color` that takes a string font color as input, and returns True if the font color is a valid hexadecimal color code, False otherwise.
"""

def validate_font_size(font_size):
    try:
        font_size = int(font_size)
        if font_size < 10 or font_size > 40:
            return False
    except ValueError:
        return False
    return True

def validate_font_color(font_color):
    if not font_color.startswith('#') or len(font_color) != 7:
        return False
    try:
        int(font_color[1:], 16)
    except ValueError:
        return False
    return True