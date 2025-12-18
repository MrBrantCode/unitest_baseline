"""
QUESTION:
Implement a function named `delete_file_system` that simulates the operation of the Unix/Linux command 'rm -rf /'. This function should take in a file system represented as a nested dictionary, delete all files and directories recursively, and return the modified file system. Note that the actual file system should not be modified. 

Assumptions: 
- The input is a dictionary where each key is a directory or file name and each value is another dictionary representing the contents of that directory or an empty dictionary if it is a file.
- The function should not ask for confirmation before deleting files or directories.
"""

def delete_file_system(file_system):
    """
    Simulates the operation of the Unix/Linux command 'rm -rf /' by deleting all files and directories recursively in a given file system.

    Args:
        file_system (dict): A dictionary representing the file system where each key is a directory or file name and each value is another dictionary representing the contents of that directory or an empty dictionary if it is a file.

    Returns:
        dict: The modified file system after deleting all files and directories recursively.
    """
    # If the file system is empty, return an empty dictionary
    if not file_system:
        return {}

    # Iterate over each item in the file system
    for key in list(file_system.keys()):
        # If the item is a directory, recursively delete its contents
        if isinstance(file_system[key], dict):
            delete_file_system(file_system[key])
        # Remove the item from the file system
        del file_system[key]

    # Return the modified file system
    return file_system