"""
QUESTION:
Implement the `count_files_with_extension` function, which takes two parameters: 
- `directory_path` (string): The path of the directory to be processed.
- `file_extension` (string): The specific file extension to be counted (e.g., 'txt', 'jpg', 'csv').

The function should return the total count of files with the given file extension within the specified directory and its subdirectories. The function should utilize multi-threading if `IS_MULTITHREADING` is set to 1; otherwise, it should process the files in a single thread.
"""

import os
import concurrent.futures

def count_files_with_extension(directory_path, file_extension):
    file_count = 0
    if IS_MULTITHREADING:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for root, _, files in os.walk(directory_path):
                futures.append(executor.submit(sum, (1 for file in files if file.endswith('.' + file_extension))))
            file_count = sum(f.result() for f in futures)
    else:
        for root, _, files in os.walk(directory_path):
            file_count += sum(1 for file in files if file.endswith('.' + file_extension))
    return file_count