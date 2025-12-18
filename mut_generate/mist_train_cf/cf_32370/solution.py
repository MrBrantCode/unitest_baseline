"""
QUESTION:
Implement a function `is_valid_license_key(key: str) -> bool` that checks if a given string `key` is a valid license key. A valid license key is a string consisting only of alphanumeric characters and dashes, with the following pattern:
- The string is composed of segments separated by dashes, and each segment must contain at least one alphanumeric character.
- The first character of each segment must be an alphanumeric character.
- All letters in the string must be uppercase.
"""

def is_valid_license_key(key: str) -> bool:
    """
    Checks if a given string key is a valid license key.
    
    A valid license key is a string consisting only of alphanumeric characters and dashes,
    with the following pattern:
    - The string is composed of segments separated by dashes, and each segment must contain at least one alphanumeric character.
    - The first character of each segment must be an alphanumeric character.
    - All letters in the string must be uppercase.
    
    Args:
        key (str): The license key to check.
    
    Returns:
        bool: True if the key is valid, False otherwise.
    """
    segments = key.split('-')
    for segment in segments:
        if not segment or not segment[0].isalnum() or not segment.isupper() or not segment.replace('-', '').isalnum():
            return False
    return True