"""
QUESTION:
Write a function named combine_colors that takes two hexadecimal colors as strings of length 6 and returns a string representing the combined color in RGB format "(R,G,B)". The function combines the two colors by swapping the first two characters of each color, converting the resulting color to RGB, and then averaging the corresponding RGB values of the two colors.
"""

def combine_colors(color1, color2):
    # Convert hexadecimal colors to RGB values
    rgb1 = tuple(int(color1[i:i+2], 16) for i in (0, 2, 4))
    rgb2 = tuple(int(color2[i:i+2], 16) for i in (0, 2, 4))
    
    # Swap the first two characters of each color
    modified_color1 = color2[:2] + color1[2:]
    modified_color2 = color1[:2] + color2[2:]
    
    # Convert modified hexadecimal colors to RGB values
    modified_rgb1 = tuple(int(modified_color1[i:i+2], 16) for i in (0, 2, 4))
    modified_rgb2 = tuple(int(modified_color2[i:i+2], 16) for i in (0, 2, 4))
    
    # Calculate combined RGB values
    combined_rgb = (
        (modified_rgb1[0] + modified_rgb2[0]) // 2,
        (modified_rgb1[1] + modified_rgb2[1]) // 2,
        (modified_rgb1[2] + modified_rgb2[2]) // 2
    )
    
    # Return the combined RGB values as a string
    return "({}, {}, {})".format(*combined_rgb)