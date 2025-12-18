"""
QUESTION:
Implement the `intersperse` function to take a list of integers `numbers` and an integer `delimiter`, returning a new list with `delimiter` interspersed between each pair of consecutive elements from `numbers`.

Implement the `add_values` function to add values from the `additional_values` list to the `numbers` list at indices specified by the `positions` list and then call the `intersperse` function with this updated list.

Restrictions: 
- The `intersperse` function should not modify the original `numbers` list.
- The `add_values` function should handle cases where `positions` indices exceed the length of the `numbers` list.

Example use cases:
- `intersperse([], 4)` returns `[]`
- `intersperse([1, 2, 3], 4)` returns `[1, 4, 2, 4, 3]`
- `add_values([1, 2, 3], [5, 6], [1, 3], 4)` returns `[1, 4, 5, 4, 2, 4, 6, 4, 3]`
"""

from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Return a new list with delimiter interspersed between each pair of consecutive elements from numbers.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result


def add_values(numbers: List[int], additional_values: List[int], positions: List[int], delimiter: int) -> List[int]:
    """
    Add values from additional_values to numbers at indices specified by positions and then call intersperse with this updated list.
    """
    updated_numbers = numbers.copy()
    offset = 0
    for i, (position, value) in enumerate(zip(positions, additional_values)):
        updated_numbers.insert(position + offset, value)
        offset += 1
    return intersperse(updated_numbers, delimiter)