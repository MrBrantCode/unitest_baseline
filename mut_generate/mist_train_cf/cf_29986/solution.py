"""
QUESTION:
Write a function `get_file_paths(file_system)` that takes in a nested dictionary representing a file system, where each key is a directory and each value is either another nested dictionary or a list of files, and returns a list of all the file paths in the file system.
"""

def entrance(file_system):
    file_paths = []

    def traverse(directory, path):
        if isinstance(directory, dict):
            for key, value in directory.items():
                traverse(value, path + key + '/')
        else:
            for file in directory:
                file_paths.append(path + file)

    traverse(file_system, '')
    return file_paths