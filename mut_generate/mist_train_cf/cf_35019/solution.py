"""
QUESTION:
Write a function `findIntersection` that takes a non-empty list of sets of distinct integers as input and returns the set of elements common to all the sets. The function should handle an empty list of sets as input, returning an empty set in this case.
"""

from typing import List, Set

def findIntersection(sets: List[Set[int]]) -> Set[int]:
    if not sets:
        return set()
    
    intersection = sets[0]
    for s in sets[1:]:
        intersection = intersection.intersection(s)
    
    return intersection