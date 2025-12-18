"""
QUESTION:
Create a function named `count_file_extensions` that takes a list of file names as input and returns a dictionary containing the count of files with each unique file extension. The function should handle cases where file names may not have an extension or have multiple extensions. The input is a list of strings, and the output is a dictionary.
"""

def count_file_extensions(file_list):
    """
    Function to count the occurrences of each unique file extension in the given list of file names.

    Parameters:
    file_list (list): A list of strings representing file names.

    Returns:
    dict: A dictionary containing the count of files with each unique file extension.
    """
    extension_count = {}
    for file_name in file_list:
        file_extension = file_name.split('.')[-1]
        if file_extension:  # Check if the file name has an extension
            if '.' in file_extension:  # Handle cases with multiple extensions
                file_extension = file_extension.split('.')[-1]
            if file_extension in extension_count:
                extension_count[file_extension] += 1
            else:
                extension_count[file_extension] = 1
        else:
            if '' in extension_count:  # Handle cases where file names do not have an extension
                extension_count[''] += 1
            else:
                extension_count[''] = 1
    return extension_count