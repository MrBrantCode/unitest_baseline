"""
QUESTION:
Implement the function `count_file_extensions(file_paths)` that takes a list of strings representing file paths and returns a dictionary containing the count of files with each unique file extension. The file extension is defined as the substring following the last occurrence of the dot (.) in the file name. If a file has no extension, it should be categorized under an empty string key in the dictionary.

Input:
- `file_paths`: A list of strings representing file paths (1 <= len(file_paths) <= 10^4). Each file path is a non-empty string consisting of lowercase and uppercase letters, digits, underscores, and dots. The length of each file path does not exceed 100 characters.

Output:
- A dictionary where the keys are unique file extensions (or an empty string for files with no extension) and the values are the count of files with that extension.
"""

from typing import List, Dict

def count_file_extensions(file_paths: List[str]) -> Dict[str, int]:
    file_extension_count = {}
    for file_path in file_paths:
        file_name = file_path.split("/")[-1]  
        if "." in file_name:
            file_extension = file_name.split(".")[-1]  
        else:
            file_extension = ""  
        file_extension_count[file_extension] = file_extension_count.get(file_extension, 0) + 1
    return file_extension_count