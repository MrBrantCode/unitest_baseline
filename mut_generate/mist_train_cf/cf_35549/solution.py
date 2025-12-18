"""
QUESTION:
Implement a function `parseSoftwareVersions(pairs)` that takes a list of tuples as input, where each tuple contains two strings representing a software version and a base64-encoded string. The function should return a list of tuples, where each tuple contains the correctly formatted software version and the decoded string. Ensure that the software version is stripped of leading and trailing whitespace characters, and the base64-encoded string is decoded to a UTF-8 string if possible. If the decoding fails, replace the decoded string with the message "Invalid Base64 encoding".
"""

import base64
from typing import List, Tuple

def parse_software_versions(pairs: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    result = []
    for version, encoded_str in pairs:
        version = version.strip()
        encoded_str = encoded_str.strip()
        decoded_str = ""
        if encoded_str:
            try:
                decoded_str = base64.b64decode(encoded_str).decode('utf-8')
            except:
                decoded_str = "Invalid Base64 encoding"
        result.append((version, decoded_str))
    return result