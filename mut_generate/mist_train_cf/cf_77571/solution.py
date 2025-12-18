"""
QUESTION:
Create a function called `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as arguments. The function should return a list where the `delimiter` is inserted between each pair of consecutive integers in the `numbers` list. The function should also validate that the `numbers` list is strictly ascending. If the list is not strictly ascending, the function should return `None`.
"""

from typing import List, Optional

def entance(numbers: List[int], delimiter: int) -> Optional[List[int]]:
    """
    Amend 'delimiter' into 'numbers' between each consecutive pair. Validate if 'numbers' is strictly ascending.
    """
    if not all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)):
        return None
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimiter)
    if result:
        result.pop()  # Removes the last unwanted 'delimiter'
    return result