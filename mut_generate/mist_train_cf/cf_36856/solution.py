"""
QUESTION:
Implement a function named `find_unique_matches` that takes a list of strings and a list of compiled regular expression patterns as input. The function should find all non-overlapping matches of the patterns within the strings, and return a set of unique matches that have more than two characters and have not been previously found.
"""

import re
from typing import List, Set, Pattern

def find_unique_matches(strings: List[str], patterns: List[Pattern]) -> Set[str]:
    found = set()
    for string in strings:
        for p in patterns:
            for match in p.findall(string):
                if (len(match) > 2) and (match not in found):
                    found.add(match)
    return found