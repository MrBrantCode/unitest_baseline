"""
QUESTION:
Create two functions, `intersperse` and `add_values`. 

The `intersperse` function should accept a list of integers, `numbers`, and an integer `delimeter`. It must return a new list with the integer `delimeter` interspersed between each pair of consecutive elements from the input list `numbers`.

The `add_values` function should add values from the `additional_values` list to the `numbers` list at indices specified by the list `positions`, and then call the `intersperse` function with this updated list. The `intersperse` function should be called with the updated list and the provided `delimeter` value.

Restrictions: The function should handle cases where the input list `numbers` is empty, and it should not modify the original list.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result

def intersperse_and_add_values(numbers: List[int], additional_values: List[int], positions: List[int], delimeter: int) -> List[int]:
    numbers_copy = numbers[:]
    for pos, val in zip(positions, additional_values):
        numbers_copy.insert(pos, val)
    return intersperse(numbers_copy, delimeter)