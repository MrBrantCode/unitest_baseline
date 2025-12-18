"""
QUESTION:
Create a function `extract_keyword_counts` that takes a string `content` as input, extracts and counts the unique keywords from the string, and returns a dictionary where the keys are the unique keywords and the values are their frequencies. The input string contains a comma-separated list of keywords.
"""

from collections import Counter
import re

def extract_keyword_counts(content):
    """
    Extracts and counts the unique keywords from a string.
    
    Args:
        content (str): A comma-separated list of keywords.
    
    Returns:
        dict: A dictionary where the keys are the unique keywords and the values are their frequencies.
    """
    keywords = re.split(r',\s*', content)
    return dict(Counter(keywords))