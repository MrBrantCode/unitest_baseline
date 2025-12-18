"""
QUESTION:
Write a function called `extract_urls` that takes a string as input and returns a list of unique URLs found in the string. The function should be able to extract URLs with different protocols (e.g., http, https), subdomains, and query parameters, and handle URLs embedded within other text, URLs with punctuation marks or special characters, and URLs with non-alphanumeric characters.
"""

import re

def extract_urls(text):
    # Regular expression pattern to match URLs
    url_pattern = re.compile(r'(https?://\S+)')
    
    # Find all matches of URLs in the given text
    matches = re.findall(url_pattern, text)
    
    # Remove duplicate URLs
    unique_urls = list(set(matches))
    
    return unique_urls