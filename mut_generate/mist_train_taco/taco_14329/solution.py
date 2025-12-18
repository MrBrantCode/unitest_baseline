"""
QUESTION:
Given a string, determine if it's a valid identifier.

## Here is the syntax for valid identifiers:
* Each identifier must have at least one character.
* The first character must be picked from: alpha, underscore, or dollar sign. The first character cannot be a digit.
* The rest of the characters (besides the first) can be from: alpha, digit, underscore, or dollar sign. In other words, it can be any valid identifier character.

### Examples of valid identifiers:
* i
* wo_rd
* b2h

### Examples of invalid identifiers:
* 1i
* wo rd 
* !b2h
"""

import re

def is_valid_identifier(identifier: str) -> bool:
    """
    Determines if the given string is a valid identifier.

    Parameters:
    identifier (str): The string to be checked for validity as an identifier.

    Returns:
    bool: True if the string is a valid identifier, False otherwise.
    """
    return re.compile(r'^[a-zA-Z_\$][a-zA-Z0-9_\$]*$').match(identifier) is not None