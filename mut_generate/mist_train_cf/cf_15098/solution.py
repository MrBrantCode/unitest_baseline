"""
QUESTION:
Create a function `switch_mode` that switches between light and night modes. The function should return a boolean indicating whether the current mode is night mode and should also return the updated color scheme based on the selected color option. The function takes a boolean `isNightMode` to track the current mode and a string `colorOption` to customize the color scheme.
"""

def switch_mode(is_night_mode, color_option):
    """
    Switches between light and night modes and returns the updated color scheme.

    Args:
    is_night_mode (bool): The current mode, True for night mode and False for light mode.
    color_option (str): The selected color option.

    Returns:
    tuple: A boolean indicating the current mode and the updated color scheme.
    """
    
    # Update the mode
    is_night_mode = not is_night_mode
    
    # Define the color schemes for light and night modes
    if is_night_mode:
        color_scheme = {
            "background": "dark",
            "text": "light",
            "accent": "blue"
        }
    else:
        color_scheme = {
            "background": "light",
            "text": "dark",
            "accent": "orange"
        }
        
    # Update the color scheme based on the selected color option
    if color_option == "red":
        color_scheme["accent"] = "red"
    elif color_option == "green":
        color_scheme["accent"] = "green"
    elif color_option == "yellow":
        color_scheme["accent"] = "yellow"
        
    return is_night_mode, color_scheme