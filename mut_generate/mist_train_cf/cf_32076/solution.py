"""
QUESTION:
Implement the `find_longest_common_prefix(paths)` function, which takes a list of file paths as input and returns the longest common prefix among them. The function should be case-sensitive and handle both Unix-style and Windows-style paths. If no common prefix is found, return an empty string.
"""

import os

def find_longest_common_prefix(paths):
    if not paths:
        return ""

    # Normalize paths to handle both Unix and Windows style paths
    normalized_paths = [os.path.normpath(path) for path in paths]

    # Split paths into components
    path_components = [path.split(os.sep) for path in normalized_paths]

    # Find the shortest path to use as a reference
    shortest_path = min(path_components, key=len)

    # Iterate through the components of the shortest path to find the common prefix
    common_prefix = ""
    for i in range(len(shortest_path)):
        if all(path[i] == shortest_path[i] for path in path_components):
            common_prefix += shortest_path[i] + os.sep
        else:
            break

    return common_prefix