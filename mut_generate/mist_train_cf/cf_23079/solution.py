"""
QUESTION:
Write a function `align_text_to_right` that takes two parameters: `screen_width` and `text`. The function should return the given `text` aligned to the right side of a screen of `screen_width` characters. The alignment should be done programmatically without using any built-in functions or libraries that handle text alignment.
"""

def align_text_to_right(screen_width, text):
    """
    Aligns the given text to the right side of a screen of screen_width characters.

    Args:
        screen_width (int): The width of the screen in characters.
        text (str): The text to be aligned.

    Returns:
        str: The text aligned to the right side of the screen.
    """
    # Calculate the number of spaces needed to align the text to the right side
    spaces_needed = screen_width - len(text)
    
    # Return the spaces followed by the text to align it to the right side
    return " " * spaces_needed + text