"""
QUESTION:
Create a function called `format_centered` that takes three parameters: a string `text`, an integer `width`, and a string `fill_char` of length 1. The function should return a string that contains `text` centered within the specified `width` and surrounded by `fill_char`. The `fill_char` should fill any remaining space around the centered `text`.
"""

def format_centered(text, width, fill_char):
    remaining_space = width - len(text)
    left_space = remaining_space // 2
    right_space = remaining_space - left_space
    centered_text = f'{fill_char * left_space}{text}{fill_char * right_space}'
    return centered_text