"""
QUESTION:
Implement a function `get_unique_index_names(indexes: List[Dict[str, str]]) -> List[str]` that takes a list of dictionaries `indexes` as input, where each dictionary contains a key "name" representing the index name. The function should filter out any duplicate index names and return the unique names in a sorted list.
"""

from typing import List, Dict

def get_unique_index_names(indexes: List[Dict[str, str]]) -> List[str]:
    unique_names = set()
    for index in indexes:
        unique_names.add(index['name'])
    return sorted(list(unique_names))