"""
QUESTION:
Write a function `group_files_by_extension(file_names)` that takes a list of file names as input, where each file name consists of a name and an extension separated by a dot, and returns a dictionary where the keys are the extensions in lowercase and the values are lists of file names with that extension.
"""

def group_files_by_extension(file_names):
    file_groups = {}
    for file_name in file_names:
        name, extension = file_name.rsplit('.', 1)
        extension = extension.lower()  # Convert the extension to lowercase
        if extension in file_groups:
            file_groups[extension].append(file_name)
        else:
            file_groups[extension] = [file_name]
    return file_groups