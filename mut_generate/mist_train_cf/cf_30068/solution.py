"""
QUESTION:
Create a function `extract_text_from_html(html_string)` that takes a string of well-formed HTML as input and returns a list of text content found within the HTML tags. The HTML tags do not contain attributes and the text content does not contain HTML tags or special characters. The function should return all the text content found within the HTML tags.
"""

from typing import List
import re

def extract_text_from_html(html_string: str) -> List[str]:
    pattern = r">([^<]+)<"
    matches = re.findall(pattern, html_string)
    return matches