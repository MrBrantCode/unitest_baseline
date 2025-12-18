"""
QUESTION:
Write a function `extract_domain_names` that takes a string `text` as input and returns a list of unique domain names extracted from the URLs present in the text. The function should consider URLs with different formats, such as "http://", "https://", and "www.".
"""

import re

def extract_domain_names(text):
    urls = re.findall(r'https?://(?:www\.)?([a-zA-Z0-9.-]+)', text)
    domain_names = list(set(urls))  # Convert to set to remove duplicates, then back to list
    return domain_names