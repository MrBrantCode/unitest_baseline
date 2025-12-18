"""
QUESTION:
Write a function called `extract_urls` to find all URLs from a given string. The function should take a string as input and return a list of URLs found in the string. The URLs may be HTTP or HTTPS and may contain special characters.
"""

import re

def extract_urls(s):
    """
    This function finds all URLs from a given string.
    
    Parameters:
    s (str): The input string to search for URLs.
    
    Returns:
    list: A list of URLs found in the string.
    """
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', s)