"""
QUESTION:
Implement the function `count_major_versions(versions)` which takes a list of strings representing programming language versions in the format "x.y" where x and y are integers. The function should return a dictionary where the keys are the major versions (the first digit of the version string) and the values are the count of occurrences of each major version. The input list contains 1 to 1000 elements, with major version numbers ranging from 1 to 99 and minor version numbers ranging from 0 to 99.
"""

from typing import List, Dict

def count_major_versions(versions: List[str]) -> Dict[str, int]:
    major_versions_count = {}
    for version in versions:
        major_version = version.split('.')[0]
        if major_version in major_versions_count:
            major_versions_count[major_version] += 1
        else:
            major_versions_count[major_version] = 1
    return major_versions_count