"""
QUESTION:
Create a function `list_modified_files` that accepts three parameters: `directory_path`, `start_time`, and `end_time`. The function should traverse the directory specified by `directory_path` and its subdirectories to identify files that have been modified within the time range defined by `start_time` and `end_time`, both in Unix timestamp format. The function should return a list of file paths that have been modified within the specified time range.
"""

import os

def list_modified_files(directory_path, start_time, end_time):
    modified_files = []

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            modification_time = os.path.getmtime(file_path)
            if start_time <= modification_time <= end_time:
                modified_files.append(file_path)

    return modified_files