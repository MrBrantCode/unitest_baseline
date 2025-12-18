"""
QUESTION:
Implement the function get_positive_and_sort_dict that takes a hierarchical dictionary where the keys are strings and the values are dictionaries with string keys and list values. The function should return a new dictionary with the same structure, but with the list values filtered to only include positive numbers and sorted in ascending order. Implement a helper function get_positive_sorted to achieve this.
"""

import typing

def get_positive_and_sort_dict(d: dict) -> typing.Dict[str, typing.Dict[str, list]]:
    def get_positive_sorted(lst: list) -> list:
        return sorted([i for i in lst if isinstance(i, (int, float)) and i > 0])

    for k, v in d.items():
        for sub_k, sub_v in v.items():
            d[k][sub_k] = get_positive_sorted(sub_v)

    return d