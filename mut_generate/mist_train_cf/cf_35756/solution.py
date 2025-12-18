"""
QUESTION:
Write a function `extract_copyright_notice` that takes a string representing the source code file as input and returns the extracted copyright notice as a string. The copyright notice should include the copyright year(s), the company name, and it must be in a comment at the beginning of the file. The function should assume that the copyright notice will always be present in the source code file and will follow a format that starts with "Copyright" followed by the year(s) and company name.
"""

import re

def extract_copyright_notice(source_code):
    match = re.search(r'Copyright\s+\d{4}-\w+\s+.*', source_code)
    if match:
        return match.group().lstrip('#').strip()
    else:
        return "Copyright notice not found"