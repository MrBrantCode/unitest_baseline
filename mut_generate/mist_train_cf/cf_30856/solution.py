"""
QUESTION:
Write a function `extract_span_content(html_txt: str) -> List[str]` where `html_txt` is a string containing valid HTML text with one or more `<span>` tags. The function should return a list of strings containing the text within the `<span>` tags in the order they appear in the HTML text. The length of `html_txt` is between 1 and 10^5, and the HTML text may contain newlines and spaces within and between the `<span>` tags.
"""

from typing import List
import re

def extract_span_content(html_txt: str) -> List[str]:
    return re.findall(r'<span.*?>(.*?)</span>', html_txt, re.DOTALL)