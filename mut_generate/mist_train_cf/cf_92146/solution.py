"""
QUESTION:
Write a function named `extract_h1_content` to extract the content between the <h1> and </h1> tags from a given HTML string and return it in reverse order. The function should take a string of HTML code as input.
"""

import re

def extract_h1_content(html_code):
    """
    Extracts the content between the <h1> and </h1> tags from a given HTML string and returns it in reverse order.

    Args:
        html_code (str): A string of HTML code.

    Returns:
        list: A list of strings representing the content between the <h1> and </h1> tags in reverse order.
    """

    # Extract the content between the <h1> and </h1> tags
    content = re.findall(r'<h1>(.*?)</h1>', html_code)

    # Reverse the order of the extracted content
    content.reverse()

    return content