"""
QUESTION:
Implement a function `extract_version_number` that takes a string as input and returns the extracted version number as a string. The version number should be in the format "x.y.z" (major.minor.patch), optionally followed by a pre-release version and build metadata. The pre-release version should start with a hyphen followed by alphanumeric characters and periods, and the build metadata should start with a plus sign followed by alphanumeric characters and periods. If the input string does not contain a valid version number, the function should return "Invalid version number".
"""

import re

def extract_version_number(input_string):
    pattern = r'\b\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?(?:\+[a-zA-Z0-9.-]+)?\b'
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return "Invalid version number"