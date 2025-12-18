"""
QUESTION:
Implement a function named `count_file_extensions` that takes a list of file names as input and returns a dictionary containing the count of each unique file extension, ignoring case and considering files without an extension as "no_extension".
"""

from typing import List, Dict
import os

def count_file_extensions(file_list: List[str]) -> Dict[str, int]:
    extension_count = {}
    for file_name in file_list:
        _, file_extension = os.path.splitext(file_name)
        if file_extension:
            file_extension = file_extension[1:].lower()  # Remove the dot and convert to lowercase
        else:
            file_extension = 'no_extension'
        extension_count[file_extension] = extension_count.get(file_extension, 0) + 1
    return extension_count