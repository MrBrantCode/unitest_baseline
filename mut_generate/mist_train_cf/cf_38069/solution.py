"""
QUESTION:
Write a function `extractPermissions` that takes a string `license_text` as input, extracts lines starting with "///", removes the leading "///" and any leading or trailing whitespace, and returns a list of the extracted permissions.
"""

from typing import List

def extractPermissions(license_text: str) -> List[str]:
    permissions = []
    lines = license_text.split("\n")
    for line in lines:
        if line.startswith("///"):
            permission = line[3:].strip()
            permissions.append(permission)
    return permissions