"""
QUESTION:
Write a function `extract_metadata(code_snippet: str) -> dict` that takes a code snippet as input and returns a dictionary containing the extracted metadata information. The metadata information is stored in the format `__<metadata_key>__ = "<metadata_value>"`, where the keys include `__title__`, `__description__`, `__url__`, and `__version__`. If a metadata key is not present in the code snippet, it should not be included in the returned dictionary.
"""

import re

def extract_metadata(code_snippet: str) -> dict:
    metadata = {}
    metadata_pattern = r'__(\w+)__ = "(.*?)"'
    matches = re.findall(metadata_pattern, code_snippet)
    
    for key, value in matches:
        metadata[key] = value
    
    return metadata