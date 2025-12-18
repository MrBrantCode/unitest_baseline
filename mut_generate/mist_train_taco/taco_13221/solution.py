"""
QUESTION:
Basic regex tasks. Write a function that takes in a numeric code of any length. The function should check if the code begins with 1, 2, or 3 and return `true` if so. Return `false` otherwise. 

You can assume the input will always be a number.
"""

def validate_numeric_code(code: int) -> bool:
    """
    Validates if the given numeric code starts with 1, 2, or 3.

    Parameters:
    code (int): The numeric code to be validated.

    Returns:
    bool: True if the code starts with 1, 2, or 3, False otherwise.
    """
    return str(code).startswith(('1', '2', '3'))