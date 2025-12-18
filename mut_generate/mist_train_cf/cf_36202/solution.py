"""
QUESTION:
Write a function `count_file_types` that takes a list of file paths as input and returns a dictionary containing the count of different file types present in the list, where file types are determined by their extensions. Ignore any file paths that do not have an extension.
"""

def count_file_types(file_paths: list) -> dict:
    file_type_count = {}
    for file_path in file_paths:
        file_name = file_path.split('/')[-1]
        if '.' in file_name:
            file_extension = file_name.split('.')[-1]
            file_type_count[file_extension] = file_type_count.get(file_extension, 0) + 1
    return file_type_count