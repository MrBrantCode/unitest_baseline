"""
QUESTION:
Write a function `longestCommonDirectoryPath` that takes a list of file paths as strings and returns the longest common directory path shared by all the file paths. Each file path consists of a list of directories separated by slashes ("/"). If there is no common directory path, return an empty string. The function should ignore the trailing slash in the output.
"""

from typing import List

def longestCommonDirectoryPath(paths: List[str]) -> str:
    if not paths:
        return ""

    split_paths = [path.split("/") for path in paths]
    min_length = min(len(path) for path in split_paths)

    common_path = ""
    for i in range(min_length):
        if all(split_path[i] == split_paths[0][i] for split_path in split_paths):
            common_path += split_paths[0][i] + "/"
        else:
            break

    return common_path.rstrip("/")