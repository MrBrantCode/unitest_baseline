"""
QUESTION:
Create a function `organize_files(file_paths)` that takes a list of file paths as input, where each file path is a string and the directory structure is delimited by forward slashes ("/"). The function should group the file paths based on their directory structure and return the hierarchical organization of the file paths.
"""

def organize_files(file_paths):
    file_structure = {}

    for path in file_paths:
        components = path.split('/')
        current_level = file_structure

        for component in components:
            if component not in current_level:
                current_level[component] = {}
            current_level = current_level[component]

    return file_structure