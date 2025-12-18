"""
QUESTION:
Create a function `replace_identifiers` that takes a string `text` as input, detects any occurrences of email addresses, URLs, and IP addresses (both IPv4 and IPv6) within the text, and replaces them with the string literals "EMAIL", "URL", and "IP_ADDR" respectively. The function should not rely on any external libraries and must have a time complexity of O(n), where n is the length of the input string. The function should account for real-world variations of these identifiers.
"""

import re

def replace_identifiers(text: str) -> str:

    # Match one of the below
    # 1. a IPv4 address
    # 2. a IPv6 address
    ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b|\\b(?:(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4})\\b'
    
    # Match a URL
    url_pattern = r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))'
    
    # Match an Email
    email_pattern = r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    
    # substitution
    text = re.sub(ip_pattern, 'IP_ADDR', text)
    text = re.sub(url_pattern, 'URL', text)
    text = re.sub(email_pattern, 'EMAIL', text)
    
    return text