"""
QUESTION:
Create a function `extractHTMLText` that takes a string `htmlCode` as input and returns a list of text content extracted from the HTML tags. The function should ignore any HTML attributes and only focus on extracting the text content within the tags. The input string will contain HTML code with various tags.
"""

from typing import List
import re

def extractHTMLText(htmlCode: str) -> List[str]:
    pattern = r">([^<]+)<"
    matches = re.findall(pattern, htmlCode)
    return matches