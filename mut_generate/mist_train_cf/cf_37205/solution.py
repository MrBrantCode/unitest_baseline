"""
QUESTION:
Write a Python function `mv_command(source, destination, interactive=False)` that takes three parameters: 
- `source`: A string representing the path to the source file or directory.
- `destination`: A string representing the path to the destination file or directory.
- `interactive`: A boolean flag indicating whether interactive prompting is enabled (default is `False`).

The function should move or rename the file or directory at `source` to `destination`. If `destination` is a directory, the file or directory at `source` should be moved into that directory. If `destination` is a file and it already exists, the function should prompt the user for confirmation before overwriting the file if `interactive` is `True`, and overwrite the file without prompting if `interactive` is `False`. If the operation is successful, the function should return `True`; otherwise, it should return an error message.
"""

import os
import shutil

def mv_command(source, destination, interactive=False):
    if not os.path.exists(source):
        return f"Error: Source '{source}' does not exist."

    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

    if os.path.exists(destination):
        if interactive:
            response = input(f"Overwrite '{destination}'? (y/n): ")
            if response.lower() != 'y':
                return "Operation canceled by user."
        else:
            try:
                os.remove(destination)
            except OSError:
                return f"Error: Could not overwrite '{destination}'."

    try:
        shutil.move(source, destination)
        return True
    except (shutil.Error, OSError) as e:
        return f"Error: {e}"