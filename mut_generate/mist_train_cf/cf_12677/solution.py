"""
QUESTION:
Create a function `wrap_text_in_box(text, length, padding)` that takes in a string `text`, a positive integer `length`, and a positive integer `padding`. The function should return a string representing the input `text` centered within a box of ASCII characters with the specified `length` and `padding`. The box's width is determined by `length + (padding * 2)`. If `length` or `padding` is not a positive integer, the function should return an error message.
"""

def entance(text, length, padding):
    if length <= 0 or padding <= 0:
        return "Length and padding parameters must be positive integers."
    
    box_length = length + (padding * 2)
    
    horizontal_line = '*' * box_length
    vertical_padding = '*' + ' ' * (box_length - 2) + '*'
    centered_text = '*' + ' ' * padding + text.center(length) + ' ' * padding + '*'
    
    box = horizontal_line + '\n' + vertical_padding + '\n' + centered_text + '\n' + vertical_padding + '\n' + horizontal_line
    
    return box