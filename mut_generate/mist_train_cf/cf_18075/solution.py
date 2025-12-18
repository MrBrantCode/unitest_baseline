"""
QUESTION:
Create a function called `rgb_to_hex` that takes a tuple of integers representing RGB color values, optionally followed by an alpha value, and returns the corresponding HEX color code as a string. The function should handle alpha values and include them in the HEX code if they are not fully opaque (255). The input tuple can have either 3 (RGB) or 4 (RGBA) elements.
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