"""
QUESTION:
Implement a function/class, which should return an integer if the input string is in one of the formats specified below, or `null/nil/None` otherwise.

Format:
* Optional `-` or `+`
* Base prefix `0b` (binary), `0x` (hexadecimal), `0o` (octal), or in case of no prefix decimal.
* Digits depending on base

Any extra character (including whitespace) makes the input invalid, in which case you should return `null/nil/None`.

Digits are case insensitive, but base prefix must be lower case.

See the test cases for examples.
"""

import re

def parse_integer(input_string: str) -> int:
    # Regular expression to match the specified formats
    if re.match(r'\A[+-]?(\d+|0b[01]+|0o[0-7]+|0x[0-9a-fA-F]+)\Z', input_string):
        # Convert the matched string to an integer
        return int(input_string, 10 if input_string[1:].isdigit() else 0)
    # Return None if the input string does not match the format
    return None