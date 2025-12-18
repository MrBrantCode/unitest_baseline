"""
QUESTION:
Write a function named `generate_textbox_html` that takes a string as input and returns the HTML code for a textbox where the ID of the textbox is equal to the input string. The function should return the HTML code as a string.
"""

def generate_textbox_html(input_string):
    textbox_html = f'<input type="text" id="{input_string}">'
    return textbox_html