"""
QUESTION:
Implement a function `extract_license_info` that takes a string `source_code` representing the source code of a project and returns a dictionary containing the extracted open-source license information. The dictionary should have the following structure: `{"license_type": string, "license_url": string}`. If the license information is not found in the source code, the function should return an empty dictionary `{}`. The function should be able to handle different types of open-source licenses and variations in the way the license information is specified within the comments.
"""

import re

def extract_license_info(source_code: str) -> dict:
    license_info = {}

    # Regular expression pattern to match license information in comments
    pattern = r'(?<=开源协议：)([\w-]+)(?:\s*\(.*\))?\s*（(http[s]?:\/\/[^\s\)]+)）'

    match = re.search(pattern, source_code)
    if match:
        license_info["license_type"] = match.group(1)
        license_info["license_url"] = match.group(2)

    return license_info