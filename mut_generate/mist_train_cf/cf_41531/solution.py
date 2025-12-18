"""
QUESTION:
Write a function `filterFiles` that takes a list of file content types as input, removes any files with content type "image/svg+xml" from the list, and only considers files with a non-empty content type for processing. The function should return a new list containing the filtered file content types.

Input: A list of file content types where each content type is a string.
Output: A new list of file content types without "image/svg+xml" and empty strings.
Restriction: The function should ignore empty strings in the input list and exclude them from the output list.
"""

from typing import List

def filterFiles(fileTypes: List[str]) -> List[str]:
    return [ftype for ftype in fileTypes if ftype and ftype != "image/svg+xml"]