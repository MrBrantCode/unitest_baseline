"""
QUESTION:
Create a regular expression that matches the specific text following a percent sign (%) in a given string, considering that the text may be immediately adjacent to the percent sign or separated by a single whitespace character, and may be followed by either a whitespace or a colon. The matched text should consist of one or more alphabetic characters.
"""

import re

def extract_text_after_percent_sign(text):
    match = re.search(r'%[\s]?([a-zA-Z]+)[\s:]', text)
    if match:
        return match.group(1)