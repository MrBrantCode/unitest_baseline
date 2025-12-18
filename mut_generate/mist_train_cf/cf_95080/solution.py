"""
QUESTION:
Write a function called `extract_bold_text` that takes an HTML string as input and returns a list of strings representing the text within the `<b>` tags, without using any built-in HTML parsing libraries or functions. The function should handle cases where there are multiple occurrences of bold text in the HTML code.
"""

import re

def extract_bold_text(html_code):
    """
    Extracts the text within the <b> tags from the given HTML code.

    Args:
        html_code (str): The input HTML code.

    Returns:
        list: A list of strings representing the text within the <b> tags.
    """

    # Regular expression to match the bold tags and extract the text within them
    pattern = r'<b>(.*?)<\/b>'

    # Find all occurrences of the pattern in the HTML code
    matches = re.findall(pattern, html_code)

    return matches