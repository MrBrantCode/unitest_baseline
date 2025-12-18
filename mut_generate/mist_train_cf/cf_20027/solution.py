"""
QUESTION:
Write a Python function named `common_keywords` that takes two strings as input, extracts common keywords from them, and returns the common keywords in a sorted list. The function should be case-insensitive and exclude punctuation marks from the resulting list. The common keywords should be identified by exact word matches, and duplicates should be removed from the resulting list.
"""

import re

def common_keywords(string1, string2):
    # Remove punctuation marks using regular expression
    string1 = re.sub(r'[^\w\s]', '', string1)
    string2 = re.sub(r'[^\w\s]', '', string2)
    
    # Convert the strings to lowercase and split into words
    words1 = string1.lower().split()
    words2 = string2.lower().split()
    
    # Remove duplicates and find the common keywords
    common_keywords = sorted(set(words1) & set(words2))
    
    return common_keywords