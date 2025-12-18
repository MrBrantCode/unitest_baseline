"""
QUESTION:
Extract the extension from a given filename string with the following requirements and restrictions:
- The filename must start with a letter.
- The filename can only contain alphanumeric characters and underscores.
- The extension must be either "txt", "csv", "xlsx", or "json".
- The filename must contain at least one uppercase letter, one lowercase letter, and one special character.
- If any of the requirements are not met, return an error message indicating the specific violation.

Function Name: extract_extension
"""

import re

def extract_extension(filename: str) -> str:
    """
    Extracts the extension from a given filename string and validates the requirements.

    Args:
    filename (str): The filename string.

    Returns:
    str: The extracted extension or an error message.
    """

    # Validate the filename
    if not filename[0].isalpha():
        return "Error: Filename must start with a letter"
    elif not re.match("^[a-zA-Z0-9_]+.[a-zA-Z0-9_]+$", filename):
        return "Error: Filename can only contain alphanumeric characters and underscores"
    elif not filename.endswith(".txt") and not filename.endswith(".csv") and not filename.endswith(".xlsx") and not filename.endswith(".json"):
        return "Error: Invalid extension. Valid extensions are 'txt', 'csv', 'xlsx', or 'json'"
    elif not any(char.islower() for char in filename[:-4]) or not any(char.isupper() for char in filename[:-4]) or not any(not char.isalnum() and char != "_" for char in filename[:-4]):
        return "Error: Filename must contain at least one uppercase letter, one lowercase letter, and one special character"
    else:
        # Extract the extension
        extension = filename.split(".")[-1]
        return extension