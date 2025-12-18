"""
QUESTION:
Implement a Python class named `Backup` with an `__init__` method that takes four parameters: `included_folders`, `excluded_folders`, `output_dir`, and `size_limit`. The `Backup` class should have a `__len__` method that calculates the total size of the backup, excluding the size of the excluded folders, and a `backup` method that performs a backup operation and checks if the size of the backup exceeds the specified `size_limit`.
"""

import os

def calculate_backup_size(included_folders, excluded_folders, output_dir, size_limit):
    total_size = 0
    for directory in included_folders:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if not any(excluded_folder in filepath for excluded_folder in excluded_folders):
                    total_size += os.path.getsize(filepath)
    if total_size > size_limit:
        print(f"Backup size exceeds the specified limit of {size_limit} bytes.")
    else:
        print("Backup completed successfully.")
    return total_size