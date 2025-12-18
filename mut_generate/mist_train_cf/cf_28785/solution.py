"""
QUESTION:
Write a function `count_files(file_system)` that takes a nested dictionary `file_system` as input where each key represents a directory and the corresponding value is either another nested dictionary (representing a subdirectory) or a string (representing a file), and returns the total number of files present in the file system.
"""

def entrance(file_system):
    total_files = 0
    for item in file_system.values():
        if isinstance(item, dict):
            total_files += entrance(item)
        else:
            total_files += 1
    return total_files