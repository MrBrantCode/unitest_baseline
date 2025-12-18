"""
QUESTION:
Create a function `build_file_system` that takes a list of file paths as input and returns a dictionary representing the file system structure. Each file path is a string consisting of directories and a file name separated by a forward slash ('/'). The function should create new directories and add files to existing directories, with files represented by `None` in the dictionary. Assume the input list is non-empty and contains valid file path strings.
"""

def build_file_system(file_paths):
    file_system = {}
    for path in file_paths:
        components = path.split('/')
        current_dir = file_system
        for component in components[:-1]:  # Iterate over directories in the path
            if component not in current_dir:
                current_dir[component] = {}  # Create a new directory
            current_dir = current_dir[component]  # Move to the next directory
        current_dir[components[-1]] = None  # Add the file to the current directory
    return file_system