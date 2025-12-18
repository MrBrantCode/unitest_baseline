"""
QUESTION:
Create a function `extract_imdb_ids(directory_path)` that takes a directory path as input, walks through all the files in the directory and its subdirectories, extracts the IMDb IDs from the file names, and returns a list of tuples. Each tuple contains the full path of a file and its corresponding IMDb ID, which is everything before the first dot in the file name.
"""

import os

def extract_imdb_ids(directory_path):
    return [(os.path.join(root, name), name.split('.')[0]) 
            for root, dirs, files in os.walk(directory_path) 
            for name in files]