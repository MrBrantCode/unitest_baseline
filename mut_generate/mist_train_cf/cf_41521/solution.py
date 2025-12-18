"""
QUESTION:
Write a function `generate_indices` that takes a list of integers `arr`, a value `value`, and a tuple of indices `exclude` as input. The function should return a list of indices where `value` is found in `arr`, excluding the indices specified in `exclude`. Assume that `arr` contains only integers and `exclude` contains valid indices within the range of `arr`.
"""

from typing import List, Tuple

def generate_indices(arr: List[int], value: int, exclude: Tuple[int, ...]) -> List[int]:
    result = []
    for i in range(len(arr)):
        if arr[i] == value and i not in exclude:
            result.append(i)
    return result