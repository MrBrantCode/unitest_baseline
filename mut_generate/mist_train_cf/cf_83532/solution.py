"""
QUESTION:
Define two functions, `intersperse` and `add_values`. The `intersperse` function should take a list of integers, `numbers`, and an integer `delimiter`, and return a new list with `delimiter` inserted between each consecutive pair in `numbers`. The `add_values` function should take a list of integers, `numbers`, a list of integers, `additional_values`, a list of indices, `positions`, and an integer `delimiter`, add elements from `additional_values` to `numbers` at indices specified by `positions`, and then call `intersperse` with the updated `numbers` and `delimiter`. The lists are not modified in-place.
"""

from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i in numbers:
        result += [i, delimiter]
    return result[:-1]  

def add_values(numbers: List[int], additional_values: List[int], positions: List[int], delimiter: int) -> List[int]:
    numbers_copy = numbers.copy()
    for val,pos in zip(additional_values, positions):
        numbers_copy.insert(pos,val)
    return intersperse(numbers_copy, delimiter)