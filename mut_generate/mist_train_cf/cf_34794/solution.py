"""
QUESTION:
Write a function `find_python_files` that takes a directory path as input and returns a list of absolute paths to all Python files (with the extension ".py") present in that directory and its subdirectories. The function should not use any external libraries other than the standard library, and it should have the following signature: `def find_python_files(directory_path: str) -> List[str]`.
"""

from typing import List
import os

def find_python_files(directory_path: str) -> List[str]:
    python_files = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files