"""
QUESTION:
Create a function `right_align_text` that takes in two parameters: `screen_width` and `text`. The function should print the given text aligned to the right side of the screen without using any built-in functions or libraries for text alignment, loops, or conditional statements.
"""

def right_align_text(screen_width, text):
    """
    Aligns the given text to the right side of the screen.
    
    Args:
    screen_width (int): The total width of the screen.
    text (str): The text to be aligned.
    
    Returns:
    str: The aligned text.
    """
    # Calculate the width of the text box
    text_box_width = len(text)
    
    # Calculate the number of spaces needed to align the text box to the right side
    spaces = screen_width - text_box_width
    
    # Return the required number of spaces followed by the text
    return " " * spaces + text