"""
QUESTION:
Write a function `extract_bold_text(html_code)` that takes a string of HTML code as input and returns a list of bold text extracted from the HTML code without using any built-in HTML parsing libraries or functions. The function should handle cases where there are multiple occurrences of bold text in the HTML code and return all of them.
"""

import re

def extract_bold_text(html_code):
    """
    Extracts bold text from the given HTML code without using any built-in HTML parsing libraries or functions.

    Args:
        html_code (str): The input HTML code.

    Returns:
        list: A list of bold text extracted from the HTML code.
    """
    # Regular expression to match the bold tags and extract the text within them
    pattern = r'<b>(.*?)<\/b>'
    # Find all occurrences of the pattern in the HTML code
    matches = re.findall(pattern, html_code)
    return matches