"""
QUESTION:
Implement a function `count_file_extensions(file_list)` that takes a list of strings representing file names and returns a dictionary where keys are unique file extensions and values are their respective counts. A file extension is the part of the file name following the last occurrence of the dot ('.'); if a file name does not have an extension, its extension is considered an empty string.
"""

def count_file_extensions(file_list):
    """
    Counts the occurrences of unique file extensions in the given list of file names.

    Args:
    file_list: A list of strings representing file names.

    Returns:
    A dictionary where keys are unique file extensions and values are the count of their occurrences in the file_list.
    """
    extension_count = {}
    for file_name in file_list:
        parts = file_name.split('.')
        if len(parts) > 1:
            extension = parts[-1]
        else:
            extension = ''
        extension_count[extension] = extension_count.get(extension, 0) + 1
    return extension_count