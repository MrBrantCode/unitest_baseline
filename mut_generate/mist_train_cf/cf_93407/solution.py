"""
QUESTION:
Create a function named `validate_and_extract_extension` that takes a filename string as input and returns the file extension if the filename is valid. A valid filename must start with a letter, contain only alphanumeric characters and underscores, and have an extension of either "txt", "csv", or "xlsx".
"""

import re

def validate_and_extract_extension(filename):
    """
    Validate a filename and extract its extension.

    Args:
    filename (str): The filename to be validated and extracted.

    Returns:
    str: The file extension if the filename is valid. Otherwise, returns None.
    """
    # Validate the filename
    if re.match(r"^[a-zA-Z][\w]*\.(txt|csv|xlsx)$", filename):
        # Extract the extension
        return filename.split(".")[-1]
    else:
        return None