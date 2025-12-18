"""
QUESTION:
Write a function named `count_div_tags` that takes an HTML string as input and returns a tuple containing two integers. The first integer is the count of opening `<div>` tags, and the second integer is the count of closing `</div>` tags.
"""

from typing import Tuple

def count_div_tags(html_snippet: str) -> Tuple[int, int]:
    opening_count = html_snippet.count('<div>')
    closing_count = html_snippet.count('</div>')
    return opening_count, closing_count