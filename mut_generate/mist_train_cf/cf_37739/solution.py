"""
QUESTION:
Implement a function `countUniqueHtmlTags(html)` that takes a string `html` representing an HTML document and returns the count of unique HTML tags present in the document. The function should consider tags with different attributes or self-closing tags as unique, and it should return the total count of distinct tags.
"""

import re

def countUniqueHtmlTags(html):
    tags = re.findall(r'<[^>]+>', html)  
    unique_tags = set(tags)  
    return len(unique_tags)