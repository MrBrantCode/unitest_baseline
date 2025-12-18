"""
QUESTION:
Write a Python function named `calculate_size` that takes a directory path as an argument and returns the total size in bytes of all `.jpg` files within that directory and its subdirectories. The function should use the `os` library for file operations.
"""

import os

def calculate_size(directory='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            if file.endswith('.jpg'):
                file_path = os.path.join(dirpath, file)
                total_size += os.path.getsize(file_path)
    return total_size