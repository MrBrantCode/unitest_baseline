"""
QUESTION:
Create a function called `count_file_extensions` that takes a list of file paths as input and returns a dictionary where keys are unique file extensions (case-insensitive) and values are the count of occurrences of each file extension in the input list. The function should ignore case sensitivity when comparing file extensions.
"""

def count_file_extensions(file_paths):
    file_extension_counts = {}
    for file_path in file_paths:
        file_extension = file_path.split('.')[-1].lower()
        file_extension_counts[file_extension] = file_extension_counts.get(file_extension, 0) + 1
    return file_extension_counts