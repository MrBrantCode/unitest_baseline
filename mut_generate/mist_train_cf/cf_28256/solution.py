"""
QUESTION:
Write a function `get_hex_color(color_name)` that takes a color name as input and returns its corresponding hexadecimal value from the given list of color names and their corresponding hexadecimal values. The list is a 2D list where the second sublist contains color names and the first sublist contains corresponding hexadecimal values for some of the colors in the second sublist. If the input color name is not found in the list or does not have a corresponding hexadecimal value, the function should return "Unknown color".
"""

def get_hex_color(color_name):
    colors = [
        ["#af3a03", "#d65d0e", "#fe8019"],  # oranges
        ["black", "red", "green", "yellow", "blue", "purple", "aqua", "lightgray",
         "gray", "lightred", "lightgreen", "lightyellow", "lightblue", "lightpurple", "lightaqua", "white",
         "brightwhite", "darkred", "darkgreen", "darkyellow", "darkblue", "darkpurple", "darkaqua", "darkgray"]
    ]
    
    for color_group in colors:
        if color_name in color_group:
            if color_group.index(color_name) == 0:
                return "Unknown color"
            return color_group[color_group.index(color_name) - 1]
    return "Unknown color"