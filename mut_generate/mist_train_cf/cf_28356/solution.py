"""
QUESTION:
Create a function `extractTextFromCurlyBraces(html: str) -> List[str]` that takes a string `html` containing HTML code as input and returns a list of all the text content found within the double curly braces `{{ }}`. The function should ignore any leading or trailing whitespace within the curly braces and only extract the text content enclosed within double quotes.
"""

from typing import List
import re

def extractTextFromCurlyBraces(html: str) -> List[str]:
    pattern = r'{{\s*"(.*?)"\s*}}'  
    matches = re.findall(pattern, html)  
    return matches