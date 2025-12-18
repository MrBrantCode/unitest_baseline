"""
QUESTION:
Create a function `count_unique_major_versions` that takes a list of strings representing programming language classifiers as input and returns the count of unique major versions present in the list. Each string should follow the format "Programming Language :: Language Name :: Major Version" where the major version is an integer. The function should ignore any invalid or improperly formatted strings and consider only the unique major versions present in the list.
"""

from typing import List

def count_unique_major_versions(classifiers: List[str]) -> int:
    unique_versions = set()
    for classifier in classifiers:
        parts = classifier.split('::')
        if len(parts) == 3:
            major_version = parts[2].strip()
            if major_version.isdigit():
                unique_versions.add(int(major_version))
    return len(unique_versions)