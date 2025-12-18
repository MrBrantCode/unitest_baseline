"""
QUESTION:
Create a function called `validate_filename` that takes a filename string as input. The function should extract the extension from the filename and validate it according to the following rules: the filename must start with a letter, can only contain alphanumeric characters and underscores, and the extension must be either "txt", "csv", or "xlsx". If the filename is valid, return the extracted extension; otherwise, return "Invalid filename."
"""

import re

def validate_filename(filename):
    """
    Validate a filename and extract its extension.

    Args:
    filename (str): The filename to be validated.

    Returns:
    str: The extracted extension if the filename is valid, "Invalid filename" otherwise.
    """
    extension = filename.split(".")[-1]
    valid_filename = re.match(r"^[a-zA-Z][\w]*\.(txt|csv|xlsx)$", filename)

    if valid_filename:
        return extension
    else:
        return "Invalid filename"