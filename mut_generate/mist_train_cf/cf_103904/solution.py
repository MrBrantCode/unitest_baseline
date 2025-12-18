"""
QUESTION:
Write a function named `combine_colors` that takes two hexadecimal color strings as input and returns a new hexadecimal color string representing the average of the two input colors. The input hexadecimal strings should be in the format of RRGGBB.
"""

def combine_colors(color1, color2):
    # Convert hexadecimal strings to RGB tuples
    rgb1 = tuple(int(color1[i:i+2], 16) for i in (0, 2, 4))
    rgb2 = tuple(int(color2[i:i+2], 16) for i in (0, 2, 4))

    # Calculate the average of RGB values
    combined_rgb = tuple(int((c1 + c2) / 2) for c1, c2 in zip(rgb1, rgb2))

    # Convert RGB values to hexadecimal string
    combined_color = ''.join(format(c, '02x') for c in combined_rgb)

    return combined_color