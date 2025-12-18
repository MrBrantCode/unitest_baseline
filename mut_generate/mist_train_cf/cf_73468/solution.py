"""
QUESTION:
Create a function `is_valid_ipv6(ip)` that takes a string `ip` as input and returns a boolean indicating whether the string matches the valid IPv6 address format. The function should use regular expressions and consider the rules of a valid IPv6 address, which consists of 8 groups of four hexadecimal digits, separated by colons (:), allowing for at most one wildcard (::) that can be used to shorten the address. The function should be case-insensitive and ignore extra whitespace.
"""

import re

def is_valid_ipv6(ip):
    pattern = re.compile(r"""
        ^
        (?!.*::.*::)                    # No more than a single wildcard allowed
        (?:(?!:)|:(?=:))                # Colon can't have leading or trailing :
        (?:[0-9a-f]{0,4}:){0,7}         # Non-wildcarded blocks are 1 to 4 hex digits
        ([0-9a-f]{1,4}|(?<=:)::)(?:(?<=:)(?=:)|$)  # Last block is 1 to 4 hex digits
        $
    """, re.VERBOSE | re.IGNORECASE | re.DOTALL)

    return bool(pattern.match(ip))