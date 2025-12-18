"""
QUESTION:
Write a function `find_python_files(directory: str)` that returns a list of Python file names in the given directory and its subdirectories. The function should only include files with the '.py' extension in the output list.
"""

import os
from typing import List

def find_python_files(directory: str) -> List[str]:
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(file)
    return python_files