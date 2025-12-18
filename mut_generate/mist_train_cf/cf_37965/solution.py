"""
QUESTION:
Write a function `hexToRGB` that takes a 24-bit hexadecimal number `hexColor` as input in the format 0xRRGGBB, where RR, GG, and BB are two-digit hexadecimal numbers representing the intensity of red, green, and blue components, respectively. The function should return a tuple of three integers representing the RGB values. The input integer should be between 0x000000 and 0xFFFFFF.
"""

def hexToRGB(hexColor):
    red = (hexColor >> 16) & 0xff
    green = (hexColor >> 8) & 0xff
    blue = hexColor & 0xff
    return (red, green, blue)