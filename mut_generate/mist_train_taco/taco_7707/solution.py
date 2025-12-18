"""
QUESTION:
Implement `String#to_cents`, which should parse prices expressed as `$1.23` and return number of cents, or in case of bad format return `nil`.
"""

import re

def parse_price_to_cents(price_str: str) -> int:
    """
    Parses a price string in the format '$1.23' and returns the number of cents as an integer.
    If the input string is not in the correct format, returns None.

    :param price_str: The input price string.
    :return: The number of cents as an integer, or None if the input string is invalid.
    """
    m = re.match(r'\$(\d+)\.(\d\d)\Z', price_str)
    if m:
        return int(m.expand(r'\1\2'))
    return None