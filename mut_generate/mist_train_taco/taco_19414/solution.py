"""
QUESTION:
You should write a simple function that takes string as input and checks if it is a valid Russian postal code, returning `true` or `false`.

A valid postcode should be 6 digits with no white spaces, letters or other symbols. Empty string should also return false. 

Please also keep in mind that a valid post code **cannot start with** `0, 5, 7, 8 or 9`


## Examples

Valid postcodes:
* 198328
* 310003
* 424000

Invalid postcodes:
* 056879
* 12A483
* 1@63
* 111
"""

def is_valid_russian_postcode(postcode: str) -> bool:
    """
    Checks if the given string is a valid Russian postal code.

    A valid postcode should be 6 digits with no white spaces, letters or other symbols.
    Empty string should also return false. Additionally, a valid post code cannot start with 0, 5, 7, 8 or 9.

    Parameters:
    postcode (str): The postal code to be validated.

    Returns:
    bool: True if the postal code is valid, False otherwise.
    """
    return len(postcode) == 6 and postcode.isdigit() and (postcode[0] not in '05789')