"""
QUESTION:
Implement the `unique_directories` function, which takes a list of strings `suffixes` as input where each string consists of alphanumeric characters and forward slashes ('/'), and returns a set of unique directory paths. The input list size is between 1 and 10^5. The function should remove trailing slashes if present and consider 'dir1/' and 'dir1' as the same directory.
"""

from typing import List, Set

def unique_directories(suffixes: List[str]) -> Set[str]:
    retval = set({})
    for s in suffixes:
        if s.endswith('/'):
            retval.add(s[:-1])
        else:
            retval.add(s)
    return retval