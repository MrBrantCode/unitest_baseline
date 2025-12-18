"""
QUESTION:
Create a function named `intersperse` that takes a list of integers (which can be nested) and an integer or float delimiter as input. The function should return a new list where the delimiter is inserted between each pair of consecutive integers in the input list. If the delimiter is negative or a non-integer, it should be ignored. The function should also handle nested lists by recursively flattening them before processing.
"""

from typing import List, Union

def intersperse(numbers: List[Union[int, List[int]]], delimiter: Union[int, float]) -> List[int]:
    """
    Introduce the 'delimiter' digit amongst every couple of sequential numbers in the supplied 'numbers' list.
    Moreover, make sure to manage scenarios that involve a negative or non-integer `delimiter`.
    Also handles nested list within numbers list.
    """
    outcome = []
    flattened_numbers = []

    for num in numbers:
        if isinstance(num, list):
            flattened_numbers.extend(intersperse(num, delimiter))  # recursive flatten
        else:
            flattened_numbers.append(num)

    for i in range(len(flattened_numbers)):
        outcome.append(flattened_numbers[i])
        if i < len(flattened_numbers) - 1 and isinstance(delimiter, int) and delimiter >= 0:
            outcome.append(delimiter)

    return outcome