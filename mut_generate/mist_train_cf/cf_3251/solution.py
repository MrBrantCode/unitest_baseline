"""
QUESTION:
Write a function called `rgb_to_hex` that takes an RGB color as a tuple with three components (red, green, blue) and an optional alpha value (default 255). The function should convert the RGB color to its corresponding hexadecimal representation without using any built-in functions or libraries for color conversions, and return the HEX color code with the alpha value if it is not fully opaque.
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