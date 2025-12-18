"""
QUESTION:
Create a function named `format_filename` that takes a file path as input, extracts the filename, converts it to lowercase, replaces any whitespace characters with underscores, and returns the formatted filename with its extension. The function should not include the directory path in the output.
"""

import os

def format_filename(file_path):
    """
    Format the filename in a given file path.

    This function takes a file path, extracts the filename, converts it to lowercase, 
    replaces any whitespace characters with underscores, and returns the formatted filename with its extension.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The formatted filename with its extension.
    """
    filename_with_extension = os.path.basename(file_path)
    filename, extension = os.path.splitext(filename_with_extension)
    filename = filename.lower().replace(" ", "_")
    return f'{filename}{extension}'