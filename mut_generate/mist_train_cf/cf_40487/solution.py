"""
QUESTION:
Create a function `extract_version` that takes a string `package_name` and a string `version_string` as input. The `version_string` follows the semantic versioning format (major.minor.patch) and may contain a suffix. The function should return the version number as a string. The `package_name` can be any string, but it will not be used in the extraction process. The function should return "Version number not found" if the version number is not found in the `version_string`.
"""

import re

def extract_version(package_name: str, version_string: str) -> str:
    pattern = r"__version__ = '([\d\.]+-?\w*)'"
    match = re.search(pattern, version_string)
    if match:
        return match.group(1)
    else:
        return "Version number not found"