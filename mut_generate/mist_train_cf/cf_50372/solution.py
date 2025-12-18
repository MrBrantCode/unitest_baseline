"""
QUESTION:
Create a function `remove_duplicates` that takes a list of integers or strings `data` and an optional boolean `allow_consecutive_duplicates` with a default value of `True`. The function should return a list with duplicate elements removed, preserving the original order, and allowing consecutive duplicates if `allow_consecutive_duplicates` is `True`. The function should have a time complexity of O(n).
"""

from typing import List, Union

def remove_duplicates(data: List[Union[int, str]], allow_consecutive_duplicates: bool = True) -> List[Union[int, str]]:
    if not data:
        return []
    
    res = [data[0]]
    for i in range(1, len(data)):
        if data[i] != data[i-1] or (data[i] == data[i-1] and allow_consecutive_duplicates):
            res.append(data[i])
    return res