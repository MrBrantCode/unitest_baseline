"""
QUESTION:
Write a function named rgb_to_hex that takes a tuple of three RGB color components (red, green, blue) and an optional alpha value as input and returns the corresponding HEX color code. The function should handle alpha values and return the HEX color code with the alpha value if it is not fully opaque. Do not use any built-in functions or libraries for color conversions.
"""

def rgb_to_hex(rgb_color, alpha=255):
    hex_color = '#'
    
    # Convert RGB color to HEX
    for component in rgb_color:
        hex_component = hex(component)[2:].zfill(2)
        hex_color += hex_component
    
    # Add alpha value if not fully opaque
    if alpha < 255:
        hex_alpha = hex(alpha)[2:].zfill(2)
        hex_color += hex_alpha
    
    return hex_color