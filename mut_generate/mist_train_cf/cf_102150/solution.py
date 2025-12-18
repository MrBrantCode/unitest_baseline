"""
QUESTION:
Write a function called `process_keys` that takes a dictionary as input. The function should return a list of the dictionary's keys after converting them to uppercase, removing any special characters, and sorting them in descending order based on their length. Special characters include any non-alphanumeric characters.
"""

def process_keys(dictionary):
    """
    This function processes the keys of a dictionary by converting them to uppercase, 
    removing any special characters, and sorting them in descending order based on their length.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        list: A list of processed keys.
    """
    keys = list(dictionary.keys())
    keys = [key.upper() for key in keys]
    keys = ["".join(c for c in key if c.isalnum()) for key in keys]
    keys.sort(key=len, reverse=True)
    return keys