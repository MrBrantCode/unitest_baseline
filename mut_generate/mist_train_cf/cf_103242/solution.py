"""
QUESTION:
Create a function named `format_text` that takes two parameters: `text` and `indentation`. The function should remove consecutive duplicate characters from the input `text` and then add the specified `indentation` (number of spaces) at the beginning of the text. The function should return the formatted text as a string.
"""

def format_text(text, indentation):
    """
    Removes consecutive duplicate characters from the input text and adds the specified indentation.
    
    Args:
        text (str): The input text to be formatted.
        indentation (int): The number of spaces to be added at the beginning of the text.
    
    Returns:
        str: The formatted text.
    """
    # Remove consecutive duplicate characters
    formatted_text = ""
    prev_char = ""
    for char in text:
        if char != prev_char:
            formatted_text += char
        prev_char = char
    
    # Add indentation
    formatted_text = " " * indentation + formatted_text
    
    return formatted_text