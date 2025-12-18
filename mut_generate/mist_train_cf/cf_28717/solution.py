"""
QUESTION:
Create a function named `extract_version_info` that takes a string `code_snippet` containing version information in the format "# version: release_date." where version is a string that may contain digits, letters, and spaces, and release_date is a string in the format "Month Day, Year". Extract the version numbers and their corresponding release dates, and return them in a formatted string in the format "Version: version, Release Date: release_date".
"""

import re

def extract_version_info(code_snippet):
    pattern = r'# (\w+ \d+\.\d+(?:\s\w+)?): (\w+ \d+, \d+)'
    matches = re.findall(pattern, code_snippet)
    version_info = [f"Version: {match[0]}, Release Date: {match[1]}" for match in matches]
    return "\n".join(version_info)