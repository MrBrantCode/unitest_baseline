"""
QUESTION:
Construct a regular expression function `construct_regex` that takes a list of keywords as input and returns a regular expression pattern that fails to match any string containing these keywords. The function should escape special characters in the keywords, and the returned pattern should match any string that does not contain the keywords.
"""

import re

def construct_regex(keywords):
    """
    Construct a regular expression pattern that fails to match any string containing the given keywords.
    
    Args:
    keywords (list): A list of keywords to be excluded from the match.
    
    Returns:
    str: A regular expression pattern.
    """
    # Escape special characters in the keywords and join them with '|'
    pattern = '|'.join(re.escape(keyword) for keyword in keywords)
    
    # Construct the regular expression pattern
    regex = f'^(?!.*?({pattern})).*$'
    
    return regex