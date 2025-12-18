"""
QUESTION:
Create a function named `classify_color` that takes two parameters, `light_dark` and `warm_cool`, to determine the color classification based on the following decision tree rules. The possible values for `light_dark` are 'light' and 'dark', and the possible values for `warm_cool` are 'warm' and 'cool'. The function should return the color classification as a string. 

For light colors, the function should further ask for a third parameter, `color_type`, with possible values 'yellow', 'pink', 'light_blue', and 'light_green'. For dark warm colors, the third parameter `color_type` should have possible values 'brown' and 'red'. For dark cool colors, the third parameter `color_type` should have possible values 'dark_blue' and 'dark_green'. 

The color classifications should be returned as 'YELLOW', 'PINK', 'LIGHT BLUE', 'LIGHT GREEN', 'BROWN', 'RED', 'DARK BLUE', and 'DARK GREEN'.
"""

def classify_color(light_dark, warm_cool, color_type=None):
    """
    Classify a color based on the given parameters.

    Parameters:
    light_dark (str): 'light' or 'dark'
    warm_cool (str): 'warm' or 'cool'
    color_type (str): Specific color type based on light_dark and warm_cool.

    Returns:
    str: Color classification as 'YELLOW', 'PINK', 'LIGHT BLUE', 'LIGHT GREEN', 'BROWN', 'RED', 'DARK BLUE', and 'DARK GREEN'.
    """
    if light_dark == 'light':
        if warm_cool == 'warm':
            return 'YELLOW' if color_type == 'yellow' else 'PINK'
        else:
            return 'LIGHT BLUE' if color_type == 'light_blue' else 'LIGHT GREEN'
    else:
        if warm_cool == 'warm':
            return 'BROWN' if color_type == 'brown' else 'RED'
        else:
            return 'DARK BLUE' if color_type == 'dark_blue' else 'DARK GREEN'