"""
QUESTION:
Create a function `removeFileOrDirectory(path: str) -> str` that simulates removing a file or directory from a file system. The function takes a string `path` representing the absolute or relative file path and returns a string indicating the result of the operation. The function should handle errors and return one of the following messages:
- "File removed successfully" 
- "Directory removed successfully" 
- "File not found" 
- "Invalid path"
"""

import os

def removeFileOrDirectory(path: str) -> str:
    if not os.path.exists(path):
        return "File not found"
    try:
        if os.path.isfile(path):
            os.remove(path)
            return "File removed successfully"
        elif os.path.isdir(path):
            os.rmdir(path)
            return "Directory removed successfully"
        else:
            return "Invalid path"
    except Exception as e:
        return str(e)