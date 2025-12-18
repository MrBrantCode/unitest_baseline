"""
QUESTION:
Create a function `extract_urls` that takes a text string as input and returns a list of extracted URLs. The URLs must be in the format "http://www.example.com" or "https://www.example.com" and may contain additional query parameters or anchors. The function should be able to handle text strings with a length of up to 1 million characters in a reasonable amount of time, and the list of extracted URLs should have a maximum size of 1000. If no URLs are found, return an empty list.
"""

import re

def extract_urls(text):
    pattern = r"(https?://www\.[^\s/$.?#].[^\s]*)"
    return re.findall(pattern, text)[:1000]