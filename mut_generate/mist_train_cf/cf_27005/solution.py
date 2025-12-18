"""
QUESTION:
Write a function `countClosingTags` that takes a string `text` as input and returns the count of HTML closing tags present in the text. A closing tag is a string that starts with "</" and ends with ">". The input text is a valid string and may contain other HTML tags.
"""

import re

def count_closing_tags(text):
    closing_tags = re.findall(r'</\w+>', text)
    return len(closing_tags)