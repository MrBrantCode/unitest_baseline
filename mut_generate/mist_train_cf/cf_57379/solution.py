"""
QUESTION:
Create a function `enumerate_txt_files(directory)` that takes a directory path as an argument and returns a list of file names with the .txt extension within that directory. The function should only consider files with the .txt extension and ignore subdirectories and other file types.
"""

import os

def enumerate_txt_files(directory):
    txt_files = []  # List to store names of .txt files

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            txt_files.append(filename)
            
    return txt_files