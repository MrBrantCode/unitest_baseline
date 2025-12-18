"""
QUESTION:
Implement a function `find_all_occurrences` that finds all occurrences of a given substring `sub_string` within a larger string `main_string`. The function should return a list of indices where the substring is found. If the substring is not found, the function should return an empty list. The function should not include any index more than once in the returned list, and the indices should be in ascending order.
"""

from typing import List

def find_all_occurrences(main_string: str, sub_string: str) -> List[int]:
    occurrences = []
    last_position = -1
    while True:
        position = main_string.find(sub_string, last_position + 1)
        if position == -1:
            break
        occurrences.append(position)
        last_position = position
    return occurrences