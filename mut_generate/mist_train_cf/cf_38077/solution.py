"""
QUESTION:
Create a function `calculate_directory_size` that takes a directory path as input and returns the total size of all files within the directory, excluding any files with a ".torrent" extension. The function should traverse the directory and its subdirectories to calculate the total size.
"""

import os

def calculate_directory_size(directory_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            if not filename.endswith('.torrent'):
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
    return total_size