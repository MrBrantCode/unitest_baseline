"""
QUESTION:
Design a function `all_prefixes_with_lengths` that takes a string as input and returns a list of tuples. Each tuple should contain a prefix of the input string and the length of that prefix. The list should be in ascending order of prefix length. The function should handle strings of any length, including empty strings.
"""

from typing import List, Tuple

def all_prefixes_with_lengths(string: str) -> List[Tuple[str, int]]:
    """ 
    Function that returns a list of tuples which include all prefixes of an input string from smallest to largest and their corresponding lengths
    E.g. all_prefixes_with_lengths('abc') should return [('a', 1), ('ab', 2), ('abc', 3)]
    """
    return [(string[:i], i) for i in range(1, len(string)+1)]