"""
QUESTION:
Implement a function `dedupe_tuples` that removes duplicate tuples from a list of tuples. A tuple is considered a duplicate if it has the same elements in the same order as another tuple in the list. The function should return a new list with the duplicates removed. The input is a list of tuples and the output is a list of unique tuples.
"""

from typing import List, Tuple

def dedupe_tuples(tups: List[Tuple]) -> List[Tuple]:
    seen = set()
    result = []
    for tup in tups:
        if tup not in seen:
            result.append(tup)
            seen.add(tup)
    return result