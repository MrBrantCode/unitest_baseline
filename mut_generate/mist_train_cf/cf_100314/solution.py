"""
QUESTION:
Create a function `color_harmonies(hex_color)` that takes a single argument, a hexadecimal color code. The function should calculate and return the complementary, triadic, and analogous colors based on the input color, represented as a tuple of three lists of hexadecimal color codes. 

The input hexadecimal color code should be converted to RGB values and then to HSV values. Use the HSV values to calculate the complementary hue (H + 180°), triadic hues (H + 120° and H + 240°), and analogous hues (H ± 30°, H ± 60°, H ± 90°, and H ± 120°). 

Finally, convert the calculated hues back to RGB values and then to hexadecimal color codes.
"""

import colorsys

def color_harmonies(hex_color):
    """
    Calculate and return the complementary, triadic, and analogous colors 
    based on the input color, represented as a tuple of three lists of 
    hexadecimal color codes.

    Args:
        hex_color (str): A hexadecimal color code.

    Returns:
        tuple: A tuple containing lists of complementary, triadic, and 
        analogous colors in hexadecimal format.
    """

    # Convert the hexadecimal color code to RGB values
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    
    # Convert the RGB values to HSV values
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    
    # Calculate the complementary hue
    complementary_hue = (h + 0.5) % 1.0
    
    # Calculate the triadic hues
    triadic_hues = [(h + 1/3) % 1.0, (h + 2/3) % 1.0]
    
    # Calculate the analogous hues
    analogous_hues = [(h + 1/12) % 1.0, (h + 1/6) % 1.0, (h + 1/4) % 1.0, 
                      (h - 1/12) % 1.0, (h - 1/6) % 1.0, (h - 1/4) % 1.0]
    
    # Convert the complementary hue to RGB values
    complementary_rgb = colorsys.hsv_to_rgb(complementary_hue, s, v)
    
    # Convert the triadic hues to RGB values
    triadic_rgbs = [colorsys.hsv_to_rgb(hue, s, v) for hue in triadic_hues]
    
    # Convert the analogous hues to RGB values
    analogous_rgbs = [colorsys.hsv_to_rgb(hue, s, v) for hue in analogous_hues]
    
    # Convert the complementary RGB values to hexadecimal color code
    complementary_hex = '#{:02x}{:02x}{:02x}'.format(*[int(x*255) for x in complementary_rgb])
    
    # Convert the triadic RGB values to hexadecimal color codes
    triadic_hexes = ['#{:02x}{:02x}{:02x}'.format(*[int(x*255) for x in rgb]) for rgb in triadic_rgbs]
    
    # Convert the analogous RGB values to hexadecimal color codes
    analogous_hexes = ['#{:02x}{:02x}{:02x}'.format(*[int(x*255) for x in rgb]) for rgb in analogous_rgbs]
    
    # Return the results
    return [complementary_hex], triadic_hexes, analogous_hexes