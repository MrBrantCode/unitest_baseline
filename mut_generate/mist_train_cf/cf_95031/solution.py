"""
QUESTION:
Create a function called `rgb_to_hex` that takes a tuple representing an RGB or RGBA color as input, where each color value is an integer ranging from 0 to 255. The function should return the corresponding HEX color code as a string. If the input tuple has four values, the last value represents the alpha channel and should be included in the HEX code. If the alpha value is 255 or if the input tuple only has three values, the HEX code should not include the alpha value. Do not use any built-in functions or libraries for color conversions.
"""

def rgb_to_hex(rgb):
    # Extract the RGB values and alpha value (if present)
    r, g, b = rgb[:3]
    alpha = rgb[3] if len(rgb) == 4 else 255
    
    # Check if the alpha value is fully opaque
    if alpha == 255:
        return '#%02x%02x%02x' % (r, g, b)
    
    # Convert RGB values to HEX and append alpha value
    return '#%02x%02x%02x%02x' % (r, g, b, alpha)