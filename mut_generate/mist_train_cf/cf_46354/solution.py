"""
QUESTION:
Create a function named `pattern_match_order` that takes two parameters: a list of strings and a tuple containing a list of patterns, a prefix string, and a suffix string. The function should return a list of strings from the input list that start with the given prefix, end with the given suffix, and contain all patterns in the given order.
"""

from typing import List, Tuple

def pattern_match_order(strings: List[str], pattern: Tuple[List[str], str, str]) -> List[str]:
    """ Filter an input list of strings only for ones that contain a given sequence of patterns (in the same order), start with a given prefix, and end with a given suffix.
    The patterns must occur in the same order in the string. """

    def match_pattern(string, patterns, prefix, suffix):
        """ Check whether a string matches a pattern """
        if not (string.startswith(prefix) and string.endswith(suffix)):
            return False
        previous_index = 0
        for pattern in patterns:
            try:
                current_index = string.index(pattern, previous_index)
                previous_index = current_index + len(pattern)
            except ValueError:
                return False
        return True
        
    patterns, prefix, suffix = pattern
    return [string for string in strings if match_pattern(string, patterns, prefix, suffix)]