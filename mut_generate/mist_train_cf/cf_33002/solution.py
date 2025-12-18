"""
QUESTION:
Create a function `count_file_extensions` that takes a list of file paths as input and returns a dictionary containing the count of files grouped by their file extensions. The function should consider only the last part of the file name as the extension and handle both absolute and relative file paths. The function should return a dictionary where the keys are the file extensions and the values are the corresponding counts.
"""

from typing import List, Dict
import os

def count_file_extensions(file_paths: List[str]) -> Dict[str, int]:
    file_extension_count = {}
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lstrip('.')  # Remove the leading dot from the extension
        file_extension_count[file_extension] = file_extension_count.get(file_extension, 0) + 1
    return file_extension_count