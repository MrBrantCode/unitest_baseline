"""
QUESTION:
Implement a function `count_file_extensions` that takes a list of file paths as input and returns a dictionary containing the count of files with each unique file extension. The file extension is the substring following the last dot (.) in the file name, and an empty string if no dot is present. The function should be case-insensitive when determining file extensions.
"""

from typing import List, Dict

def count_file_extensions(file_paths: List[str]) -> Dict[str, int]:
    file_extension_count = {}
    for file_path in file_paths:
        file_name, file_extension = file_path.rsplit('.', 1) if '.' in file_path else (file_path, '')
        file_extension = file_extension.lower()
        file_extension_count[file_extension] = file_extension_count.get(file_extension, 0) + 1
    return file_extension_count