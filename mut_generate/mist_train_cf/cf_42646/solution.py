"""
QUESTION:
Write a function `remove_duplicates` that takes a list of names and a specific name to be removed as input. The function should return the modified list with all occurrences of the specific name removed, except for the first occurrence.
"""

from typing import List

def remove_duplicates(names: List[str], name_to_remove: str) -> List[str]:
    seen = set()
    result = []
    for name in names:
        if name == name_to_remove and name_to_remove not in seen:
            seen.add(name_to_remove)
            result.append(name)
        elif name != name_to_remove:
            result.append(name)
    return result