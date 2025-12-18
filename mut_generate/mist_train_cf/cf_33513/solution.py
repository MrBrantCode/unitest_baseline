"""
QUESTION:
Create a function `extract_code_info` that takes a string `file_content` as input and returns a list of dictionaries. Each dictionary should contain two keys: "language" and "generator_version". The function should extract the programming language and the version of the AutoRest Code Generator from the file content using the patterns `# coding=([\w-]+)` and `AutoRest Code Generator\.?\s?v?(\d+\.\d+\.\d+)` respectively. The function should return a list with a single dictionary if both patterns are found, otherwise an empty list.
"""

import re

def extract_code_info(file_content):
    language_pattern = re.compile(r'# coding=([\w-]+)')
    version_pattern = re.compile(r'AutoRest Code Generator\.?\s?v?(\d+\.\d+\.\d+)')
    
    language_match = language_pattern.search(file_content)
    version_match = version_pattern.search(file_content)
    
    if language_match and version_match:
        language = language_match.group(1)
        version = version_match.group(1)
        return [{"language": language, "generator_version": version}]
    else:
        return []