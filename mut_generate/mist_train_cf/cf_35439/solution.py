"""
QUESTION:
Create a function `get_recent_commits` that takes a directory path as an argument, sorts the files with a ".zip" extension in the directory based on their modification time, and returns a list of the most recent commit files. The function must be able to change the current working directory to the specified directory, perform the operation, and then change back to the original directory.
"""

import os

def get_recent_commits(directory_path):
    """
    Returns a list of the most recent commit files in the specified directory.

    Args:
    directory_path (str): The path to the directory containing commit files.

    Returns:
    list: A list of the most recent commit files in the directory.
    """
    current_directory = os.getcwd()  
    os.chdir(directory_path)  
    commit_files = [f for f in os.listdir('.') if f.endswith('.zip')]  
    sorted_commit_files = sorted(commit_files, key=lambda f: os.path.getmtime(f))  
    os.chdir(current_directory)  

    return sorted_commit_files 