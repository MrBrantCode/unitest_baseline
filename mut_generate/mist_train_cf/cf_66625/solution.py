"""
QUESTION:
Implement a function named `duplicate_detector` that takes two arguments: a list of tuples, where each tuple contains an access code (an integer) and an operation (a string), and an optional boolean flag `show_duplicates` with a default value of `False`. The function should return `True` if any duplicate access code is found, regardless of the operation, and `False` otherwise. If `show_duplicates` is `True`, the function should also print the list of duplicate access codes.
"""

def duplicate_detector(values: list[tuple[int, str]], show_duplicates: bool = False) -> bool:
    seen_values = set()
    duplicates = []

    for value in values:
        if value in seen_values:
            duplicates.append(value)
        else:
            seen_values.add(value)

    if show_duplicates and duplicates:
        print('Duplicates: ', duplicates)

    return bool(duplicates)