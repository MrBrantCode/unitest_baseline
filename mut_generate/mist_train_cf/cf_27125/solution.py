"""
QUESTION:
Implement a function `isValidFilePath` that takes a string `filePath` as input and returns a boolean indicating whether the file path is valid or not. A valid file path should not contain any of the following characters: <, >, :, ", /, \, |, ?, or *. Additionally, the file path should not end with a space or a period.
"""

import re

def isValidFilePath(filePath: str) -> bool:
    """
    Checks if a file path is valid.

    A valid file path should not contain any of the following characters: <, >, :, ", /, \, |, ?, or *.
    Additionally, the file path should not end with a space or a period.

    Args:
        filePath (str): The file path to check.

    Returns:
        bool: True if the file path is valid, False otherwise.
    """
    # Define the regular expression pattern to match invalid characters
    invalid_chars = re.compile(r'[<>:"/\\|?*]')
    
    # Check for invalid characters in the file path
    if invalid_chars.search(filePath):
        return False
    
    # Check for trailing space or period at the end of the file path
    if filePath.endswith((' ', '.')):
        return False
    
    return True