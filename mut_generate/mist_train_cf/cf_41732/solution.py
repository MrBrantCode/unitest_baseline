"""
QUESTION:
Extract the name within the `<NAME>` tag from a given HTML string, where the name is immediately followed by the word "began". The name will always appear within the `<NAME>` tag and the function should return the name if found, otherwise return "No name found". 

Implement the `extract_name_from_html(html_string)` function.
"""

import re

def extract_name_from_html(html_string):
    pattern = r'<NAME>(.*?)began'
    match = re.search(pattern, html_string)
    
    if match:
        name = match.group(1).strip()
        return name
    else:
        return "No name found"