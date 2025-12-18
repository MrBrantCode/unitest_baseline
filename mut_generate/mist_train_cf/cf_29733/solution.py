"""
QUESTION:
Write a function `extractFileExtensions` that takes a list of file paths as input, extracts the file extension from each path (defined as the substring following the last occurrence of the dot (.) character), and returns a list of corresponding file extensions. If a file path does not contain a dot or the dot is the last character in the path, consider the file extension as empty.
"""

from typing import List

def extractFileExtensions(filePaths: List[str]) -> List[str]:
    return [path.split('.')[-1] if '.' in path else '' for path in filePaths]