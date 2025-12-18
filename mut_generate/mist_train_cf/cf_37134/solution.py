"""
QUESTION:
Create a function `hex_to_rgb(color)` that takes a string `color` in the format "#RRGGBB" as input, where RR, GG, and BB are two-digit hexadecimal numbers representing the intensity of red, green, and blue, respectively. The function should return a string in the format "RGB(r, g, b)" where r, g, and b are the red, green, and blue values in the range 0-255.
"""

def hex_to_rgb(color):
    color = color.lstrip('#')
    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)
    return f"RGB({red}, {green}, {blue})"