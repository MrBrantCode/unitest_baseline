"""
QUESTION:
Write a function named `align_right` that programmatically aligns a given text to the right side of a screen of a specified width without using built-in functions or libraries that handle text alignment. The function should take two parameters: the screen width and the text to be aligned.
"""

def align_right(width, text):
    """
    Aligns the given text to the right side of a screen of a specified width.
    
    Parameters:
    width (int): The width of the screen.
    text (str): The text to be aligned.
    
    Returns:
    str: The aligned text.
    """
    spaces_needed = width - len(text)
    return " " * spaces_needed + text