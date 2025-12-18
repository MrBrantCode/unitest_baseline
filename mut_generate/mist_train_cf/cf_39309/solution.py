"""
QUESTION:
Implement a function `find_highest_versions(file_list: List[Tuple[str, int]]) -> Dict[str, int]` that takes a list of tuples, where each tuple contains a file name and a version number, and returns a dictionary containing the highest version number for each unique file name. The input list can contain duplicate file names with different version numbers, and the function should handle this by selecting the highest version number for each file name.
"""

from typing import List, Tuple, Dict

def find_highest_versions(file_list: List[Tuple[str, int]]) -> Dict[str, int]:
    highest_versions = {}
    for file, version in file_list:
        if file in highest_versions:
            highest_versions[file] = max(highest_versions[file], version)
        else:
            highest_versions[file] = version
    return highest_versions