"""
QUESTION:
Write a function `extract_license_url` that takes a string `license_text` as input. The function should return the URL of the license, which starts with "http://" or "https://" and ends with the first occurrence of a newline character. If no URL is present, it should return an empty string. Assume the input `license_text` will always contain a valid license URL.
"""

import re

def extract_license_url(license_text):
    url_match = re.search(r'(http[s]?:\/\/[^\n]+)', license_text)
    if url_match:
        return url_match.group(0)
    else:
        return ""