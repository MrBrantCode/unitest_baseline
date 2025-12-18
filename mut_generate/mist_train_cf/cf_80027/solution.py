"""
QUESTION:
Write a function `has_flag` that checks if a certain flag is set in a given flags enum value. The function should take two parameters: the flags enum value and the flag to check for. It should return `True` if the flag is set, and `False` otherwise. The function should work with enum values that have multiple flags set using bitwise OR operation.
"""

def has_flag(flags, flag):
    """
    Checks if a certain flag is set in a given flags enum value.

    Args:
        flags (int): The flags enum value.
        flag (int): The flag to check for.

    Returns:
        bool: True if the flag is set, False otherwise.
    """
    return bool(flags & flag)