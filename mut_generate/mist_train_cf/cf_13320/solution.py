"""
QUESTION:
Create a function named `rgb_to_hex(rgb)` that takes a tuple of three decimal numbers representing an RGB value and converts it into a HEX string. The function should first round each RGB value to the nearest integer, then check if the values are within the range of 0 to 255. If any value is outside this range, return an error message. Otherwise, return the HEX value as a 6-digit string preceded by a '#' symbol, padding with zeros if necessary.
"""

def entrance(rgb):
    r, g, b = map(round, rgb)
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        return "Error: RGB values must be between 0 and 255."
    
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)