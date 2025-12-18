"""
QUESTION:
Write a function called `validate_name` that takes one string argument `name` and returns a boolean value. The function should return `True` if the `name` meets all of the following requirements and `False` otherwise: 
- The `name` must be at least 5 characters long.
- The `name` must start with a capital letter.
- The `name` must contain at least one special character (!, @, #, $, %).
- The `name` must not contain any repeating characters.
- The `name` must have at least one vowel and one consonant.
"""

def validate_name(name):
    """
    Validate a name based on the following requirements:
    - The name must be at least 5 characters long.
    - The name must start with a capital letter.
    - The name must contain at least one special character (!, @, #, $, %).
    - The name must not contain any repeating characters.
    - The name must have at least one vowel and one consonant.

    Args:
        name (str): The name to be validated.

    Returns:
        bool: True if the name is valid, False otherwise.
    """

    # Requirement 1: Check length
    if len(name) < 5:
        return False

    # Requirement 2: Check capital letter at the beginning
    if not name[0].isupper():
        return False

    # Requirement 3: Check special characters
    special_chars = ['!', '@', '#', '$', '%']  # Add more special characters if needed
    has_special_char = any(char in special_chars for char in name)
    if not has_special_char:
        return False

    # Requirement 4: Check repeating characters
    if len(set(name.lower())) != len(name):
        return False

    # Requirement 5: Check vowel and consonant
    vowels = 'aeiou'
    has_vowel = any(char in vowels for char in name.lower())
    has_consonant = any(char.isalpha() and char not in vowels for char in name.lower())
    if not has_vowel or not has_consonant:
        return False

    return True