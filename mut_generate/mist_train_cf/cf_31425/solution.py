"""
QUESTION:
Write a function `longestCommonDirectory(paths)` that takes a list of full file paths as input, where each path starts with a forward slash '/' and consists of directories and a file name separated by a forward slash '/'. The function should return the longest common directory path shared by all the file paths. If there is no common directory path, the function should return an empty string. All paths are guaranteed to have at least one directory.
"""

from typing import List

def longestCommonDirectory(paths: List[str]) -> str:
    if not paths:
        return ""

    # Split each path into directories
    split_paths = [path.split('/') for path in paths]

    # Find the minimum length of paths
    min_length = min(len(path) for path in split_paths)

    # Iterate through the directories of the first path
    for i in range(min_length):
        # Check if all paths have the same directory at index i
        if not all(path[i] == split_paths[0][i] for path in split_paths):
            return '/'.join(split_paths[0][:i])

    # If all paths have the same directories up to the minimum length, return the common path
    return '/'.join(split_paths[0][:min_length])