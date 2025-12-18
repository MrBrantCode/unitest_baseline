"""
QUESTION:
Find the absolute paths of all files with specific extensions in a given directory.

The function, `find_files_with_extension(directory, extensions)`, should take two parameters: a relative directory path (`directory`) and a list of file extensions (`extensions`). It should return a list of absolute paths for files in the directory with matching extensions. The function should have a time complexity of O(n), where n is the number of files in the given directory, and a space complexity of O(1) or O(n), where n is the number of files in the result list, due to the output.
"""

import os

def find_files_with_extension(directory, extensions):
    """
    This function finds the absolute paths of all files with specific extensions in a given directory.

    Parameters:
    directory (str): A relative directory path.
    extensions (list): A list of file extensions.

    Returns:
    list: A list of absolute paths for files in the directory with matching extensions.
    """

    abs_path = os.path.abspath(directory)
    file_list = []
    
    for root, dirs, files in os.walk(abs_path):
        for file in files:
            file_ext = os.path.splitext(file)[1]
            if file_ext in extensions:
                file_list.append(os.path.join(root, file))
    
    return file_list