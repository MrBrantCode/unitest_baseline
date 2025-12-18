"""
QUESTION:
Implement a function `reverse_and_delete_dirs` that takes a list of directories `dirsFound` as input. The function should reverse the order of directories, print each directory in the reversed order, and then delete the directories in that order. The function should return the list of directories in reverse order. Note that actual directory deletion logic may need to be implemented based on the specific environment and requirements.
"""

import os

def reverse_and_delete_dirs(dirsFound):
    reversedDirs = dirsFound[::-1]
    
    for directory in reversedDirs:
        print(directory)
        
    for directory in reversedDirs:
        print(f"Deleting directory: {directory}")
        # os.rmdir(directory)  # Uncomment this line to actually delete the directory

    return reversedDirs