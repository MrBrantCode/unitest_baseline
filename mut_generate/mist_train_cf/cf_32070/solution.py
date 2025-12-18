"""
QUESTION:
Write a function `parseLicense` that takes a string representing a source code file as input, extracts license information from the comment block at the beginning of the file, and returns it as a dictionary with keys "URL", "permissions", and "limitations". If the license information is not found or is incomplete, return None.
"""

import re

def parseLicense(source_code):
    match = re.search(r'/\*(.*?)\*/', source_code, re.DOTALL)
    if match:
        license_text = match.group(1)
        url_match = re.search(r'http[s]?:\/\/\S+', license_text)
        permissions_match = re.search(r'WITHOUT\s+WARRANTIES\s+OR\s+CONDITIONS\s+OF\s+ANY\s+KIND.*?$', license_text, re.MULTILINE)
        limitations_match = re.search(r'limitations\s+under\s+the\s+License\.', license_text)
        
        if url_match and permissions_match and limitations_match:
            return {
                "URL": url_match.group(0),
                "permissions": permissions_match.group(0),
                "limitations": limitations_match.group(0)
            }
    
    return None