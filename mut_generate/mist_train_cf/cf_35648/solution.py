"""
QUESTION:
Extract the text content within `<p>` tags from a given input string. The input string contains well-formed HTML with `<p>` tags and their corresponding closing `</p>` tags, without nested HTML tags or attributes in the `<p>` tags. Implement a function `extractParagraphContent(inputString: str) -> List[str]` to return a list of strings representing the text content within the `<p>` tags.
"""

from typing import List
import re

def extractParagraphContent(inputString: str) -> List[str]:
    pattern = r'<p>(.*?)</p>'
    matches = re.findall(pattern, inputString)
    return matches