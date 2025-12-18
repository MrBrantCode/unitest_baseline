"""
QUESTION:
Implement a function `validate_semantic_version(version)` that takes a non-empty string `version` as input and returns `True` if the input string is a valid semantic version number in the format MAJOR.MINOR.PATCH, where each part is a non-negative integer with no leading zeros except for the number 0 itself, and `False` otherwise.
"""

import re

def validate_semantic_version(version):
    pattern = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$"
    return bool(re.match(pattern, version))