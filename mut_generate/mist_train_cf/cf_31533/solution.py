"""
QUESTION:
Create a function `is_valid_license` that determines whether a given software license is valid according to the Apache License, Version 2.0. A valid license should contain both the phrases "Licensed under the Apache License, Version 2.0" and "http://www.apache.org/licenses/LICENSE-2.0". The function should return "Valid" if the license is valid and "Invalid" if it is not. The input to the function will be a string representing the license text.
"""

def is_valid_license(license_text):
    """
    Checks if a given software license is valid according to the Apache License, Version 2.0.
    
    Args:
    license_text (str): The text of the license to be checked.
    
    Returns:
    str: "Valid" if the license is valid, "Invalid" otherwise.
    """
    return "Valid" if "Licensed under the Apache License, Version 2.0" in license_text and "http://www.apache.org/licenses/LICENSE-2.0" in license_text else "Invalid"