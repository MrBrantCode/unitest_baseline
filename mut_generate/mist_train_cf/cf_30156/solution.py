"""
QUESTION:
Write a function `extract_license(text: str) -> str` that takes in a string `text` and returns the extracted license information enclosed within a block comment, which starts with a line containing only "#" followed by the license text, and ends with a line containing only "#". If the input text does not contain a valid license block, the function should return "No license found".
"""

import re

def extract_license(text: str) -> str:
    match = re.search(r'#\n(.*?)\n#', text, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return "No license found"