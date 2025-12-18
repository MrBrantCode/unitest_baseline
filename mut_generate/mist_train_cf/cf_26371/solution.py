"""
QUESTION:
Create a function `append_path` that takes two parameters: `base_path` and `relative_path`. This function should combine the `base_path` and `relative_path` and return the resulting absolute path. The `base_path` and `relative_path` are both strings representing directories, and the function should handle cases where the `base_path` does or does not end with a forward slash.
"""

def append_path(base_path, relative_path):
    if base_path.endswith('/'):
        return base_path + relative_path
    else:
        return base_path + '/' + relative_path