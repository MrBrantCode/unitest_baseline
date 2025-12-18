"""
QUESTION:
Create a function `process_file_paths` that takes a list of file paths as input. The function should return a dictionary where the keys are the indices of the file paths, and the values are dictionaries containing the folder name and the file extension of each path. The function should assume that the file paths are in the format "/path/to/logs/model_folder_{index}.extension", where `{index}` is an integer. The output dictionary should have the structure: `{index: {'folder': 'model_folder_{index}', 'extension': 'extension'}}`.
"""

import os

def process_file_paths(file_paths):
    result = {}
    for idx, path in enumerate(file_paths):
        folder_name = os.path.basename(path).split('.')[0]
        extension = os.path.basename(path).split('.')[1]
        result[idx] = {'folder': folder_name, 'extension': extension}
    return result