"""
QUESTION:
Write a function named `remove_html_tags` that takes a string as input. The function should remove all HTML tags from the string, including any content inside the tags, convert any HTML entities to their corresponding characters, sort the remaining words in the string alphabetically, and capitalize each word. The function should return the resulting string.
"""

import re
from html import unescape

def remove_html_tags(string):
    string = re.sub(r'<.*?>', '', string)
    string = unescape(string)
    string = ' '.join(word.capitalize() for word in string.split())
    string = ' '.join(sorted(string.split()))
    return string