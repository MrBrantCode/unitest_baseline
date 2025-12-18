"""
QUESTION:
Write a function `fill_missing_meta` that takes a list of dictionaries as input where each dictionary contains 'name', 'price', and 'meta' information. If 'meta' is `None`, replace it with the item's 'name' in uppercase followed by ' - NEW'. Return the updated list. The input list and the output list should have the same structure, but the output list should not have any `None` 'meta' values.
"""

from typing import List, Dict, Union

def fill_missing_meta(items: List[Dict[str, Union[str, int, None]]]) -> List[Dict[str, Union[str, int, None]]]:
    for item in items:
        if item['meta'] is None:
            item['meta'] = item['name'].upper() + ' - NEW'
    return items