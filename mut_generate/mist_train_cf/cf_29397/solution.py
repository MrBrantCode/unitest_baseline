"""
QUESTION:
Write a function `calculate_total_file_size` that calculates the total size of all files within a specified directory and its subdirectories. The function should take a directory path as input and return the total size in bytes.

The function must traverse the specified directory and its subdirectories, calculate the size of each file, and sum the sizes to determine the total size. The function should return the total size as an integer representing the total number of bytes.

The input directory path should be a string. The function should return an integer representing the total size of all files in bytes.
"""

from pathlib import Path

def calculate_total_file_size(directory_path: str) -> int:
    total_size = 0
    path = Path(directory_path)
    for file in path.glob('**/*'):
        if file.is_file():
            total_size += file.stat().st_size
    return total_size