"""
QUESTION:
Cheesy Cheeseman just got a new monitor! He is happy with it, but he just discovered that his old desktop wallpaper no longer fits. He wants to find a new wallpaper, but does not know which size wallpaper he should be looking for, and alas, he just threw out the new monitor's box. Luckily he remembers the width and the aspect ratio of the monitor from when Bob Mortimer sold it to him. Can you help Cheesy out?
# The Challenge

Given an integer `width` and a string `ratio` written as `WIDTH:HEIGHT`, output the screen dimensions as a string written as `WIDTHxHEIGHT`.
"""

def calculate_screen_dimensions(width: int, ratio: str) -> str:
    """
    Calculate the screen dimensions based on the given width and aspect ratio.

    Parameters:
    - width (int): The width of the monitor.
    - ratio (str): The aspect ratio of the monitor in the format "WIDTH:HEIGHT".

    Returns:
    - str: The screen dimensions in the format "WIDTHxHEIGHT".
    """
    a, b = map(int, ratio.split(':'))
    height = int(width / a * b)
    return f'{width}x{height}'