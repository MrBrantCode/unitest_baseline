"""
QUESTION:
Create a function called `extract_latest_version` that takes a list of file paths as input and returns a list of tuples. Each tuple should contain the original file path and the extracted version number. The version number is denoted by a leading 'v' character and may be followed by a '-' character. The function should handle cases where the version number is not present or does not follow the 'v' prefix convention.
"""

from typing import List, Tuple

def extract_latest_version(file_paths: List[str]) -> List[Tuple[str, str]]:
    extracted_versions = []
    for path in file_paths:
        version_start = path.find('v')  # Find the position of 'v' in the file path
        if version_start != -1:  # If 'v' is found
            version_end = path.find('-', version_start)  # Find the position of '-' after 'v'
            if version_end != -1:  # If '-' is found
                version = path[version_start + 1:version_end]  # Extract the version substring
            else:
                version = path[version_start + 1:]  # Extract the version substring
            extracted_versions.append((path, version))  # Add the original path and extracted version to the result list
    return extracted_versions