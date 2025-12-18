"""
QUESTION:
Implement a function `find_file_path(directory_structure, file_name, current_path='')` that recursively searches for a specific file within a given directory structure and returns the full path of the file if it is found. The directory structure is represented as a nested dictionary where each key is a directory name and each value is either another nested dictionary representing a subdirectory or a list of files in that directory. Return the full path of the file if it exists, or "File not found" if it does not.
"""

def entrance(directory_structure, file_name, current_path=''):
    for key, value in directory_structure.items():
        if isinstance(value, dict):
            result = entrance(value, file_name, current_path + key + '/')
            if result:
                return result
        elif isinstance(value, list) and file_name in value:
            return current_path + key + '/' + file_name
    return "File not found"