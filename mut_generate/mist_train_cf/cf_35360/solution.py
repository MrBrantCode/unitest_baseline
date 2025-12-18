"""
QUESTION:
Implement the `find_py_files` function that recursively finds all `.py` files within a specified folder and its subfolders. The function takes a single argument `folder`, which is the absolute path of the folder to search for `.py` files. It should return a list of absolute file paths for all the `.py` files found within the specified folder and its subfolders.
"""

import os

def find_py_files(folder):
    """Recursively finds all .py files within the specified folder and its subfolders"""
    py_files = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.abspath(os.path.join(root, file)))

    return py_files