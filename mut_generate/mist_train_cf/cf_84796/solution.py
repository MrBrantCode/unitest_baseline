"""
QUESTION:
Write a function called `extract_links_and_text` that extracts both links and associated anchor text from a given HTML string using regular expressions. The function should return a list of tuples, where each tuple contains a link and its corresponding anchor text.
"""

import re

def extract_links_and_text(html):
    pattern = '<a href="(.+?)">(.+?)<\/a>'
    result = re.findall(pattern, html)
    return result