"""
QUESTION:
Implement a function `parse_http_headers(headers)` that takes a list of strings representing HTTP headers, where each string is in the format "Key:Value". The function should return a dictionary where the keys are the header names and the values are the corresponding header values. The function should handle whitespace around the colon (:) by stripping any leading or trailing whitespace from the key and value.
"""

from typing import List, Dict

def parse_http_headers(headers: List[str]) -> Dict[str, str]:
    parsed_headers = {}
    for header in headers:
        key, value = header.split(":")
        parsed_headers[key.strip()] = value.strip()
    return parsed_headers