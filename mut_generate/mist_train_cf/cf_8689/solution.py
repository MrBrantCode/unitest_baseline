"""
QUESTION:
Write a function called `align_text` that takes two parameters: `screen_width` (the total width of the screen in characters) and `text` (the text to be aligned). The function should return a string representing the given text aligned to the right side of the screen, calculated programmatically without using any built-in functions or libraries for text alignment, loops, or conditional statements.
"""

def align_text(screen_width, text):
    text_box_width = len(text)
    spaces = screen_width - text_box_width
    return " " * spaces + text