"""
QUESTION:
Create a function `extract_metadata_info` that takes a multi-line string `code_snippet` as input, extracts metadata information in the format `__<metadata>__ = "<value>"` and returns a dictionary containing the extracted metadata information. The dictionary keys should be `copyright`, `version`, `author`, `email`, and `url`, and the corresponding values are the extracted metadata values from the code snippet.
"""

import re

def extract_metadata_info(code_snippet):
    metadata = {}
    pattern = r'__(\w+)__\s*=\s*"([^"]+)"'
    matches = re.findall(pattern, code_snippet)
    for match in matches:
        metadata[match[0]] = match[1]
    return metadata