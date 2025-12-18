"""
QUESTION:
Write a function named `extract_urls` that takes a string as input and returns a list of unique URLs found in the string. The function should be able to handle various types of URLs, including those with different protocols (e.g., http, https), subdomains, and query parameters. It should also correctly handle URLs embedded within other text, edge cases such as URLs preceded or followed by punctuation marks or special characters, and URLs containing non-alphanumeric characters.
"""

import re

def extract_urls(string):
    # Regular expression pattern to match URLs
    pattern = r'(https?://\S+)'
    
    # Find all URLs in the string using regex
    urls = re.findall(pattern, string)
    
    # Remove duplicates from the list of URLs
    unique_urls = list(set(urls))
    
    return unique_urls