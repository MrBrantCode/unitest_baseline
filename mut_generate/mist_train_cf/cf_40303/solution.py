"""
QUESTION:
Write a function called `find_test_files` that takes a directory path as a string argument. The function should return a list of all Python test files present in the specified directory and its subdirectories. A Python test file is defined as a file whose name starts with "test_" and has a ".py" extension. The function should not use any external libraries or modules beyond the Python Standard Library.
"""

import os

def find_test_files(directory):
    test_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                test_files.append(os.path.relpath(os.path.join(root, file), directory))
    return test_files