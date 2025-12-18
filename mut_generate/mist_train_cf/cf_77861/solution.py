"""
QUESTION:
Write a function named `extract_text_from_html` that takes a string containing HTML encoded syntax as input and returns the text constituents isolated from the HTML tags. The function should not use any external libraries other than those available in the Python Standard Library or the `html.parser` library.
"""

from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = ''

    def handle_data(self, data):
        self.text += data

def extract_text_from_html(html_string):
    """
    Extracts the text constituents from an HTML string.

    Args:
    html_string (str): The input HTML string.

    Returns:
    str: The text extracted from the HTML string.
    """
    parser = TextExtractor()
    parser.feed(html_string)
    return parser.text