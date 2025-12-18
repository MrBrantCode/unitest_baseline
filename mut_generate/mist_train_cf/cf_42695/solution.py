"""
QUESTION:
Write a function `get_dir_data` that takes a directory path as input, traverses the directory and its subdirectories, and returns a JSON object containing the names of files and subfolders in each folder. The function should also log the processing of the specified folder using the `logging` module. The returned JSON object should be a list of dictionaries, where each dictionary contains the relative path of a folder, a list of its files, and a list of its subfolders.
"""

import os
import logging

# Logging template
LOGGING_INFO_FOLDER_PROCESSING = "Processing folder: $folder"

def get_dir_data(directory):
    logging.info(LOGGING_INFO_FOLDER_PROCESSING.replace("$folder", directory))
    file_folder_data = []
    for root, dirs, files in os.walk(directory):
        folder_info = {
            "folder_name": os.path.relpath(root, directory),
            "files": files,
            "subfolders": dirs
        }
        file_folder_data.append(folder_info)
    return file_folder_data