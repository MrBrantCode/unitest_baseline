"""
QUESTION:
Write a function `sort_list` that takes a list containing both integers and strings as input. The function should sort the integers in ascending order based on their numeric values and the strings in alphabetical order, while maintaining the original order of elements with the same numeric or alphabetical value. The function should handle the case where the input list is empty and return an empty list in such cases.
"""

def sort_list(lst):
    if len(lst) == 0:
        return lst

    integers = sorted([item for item in lst if isinstance(item, int)])
    strings = sorted([item for item in lst if isinstance(item, str)])

    result = []
    for item in lst:
        if isinstance(item, int):
            result.append(integers.pop(0))
        elif isinstance(item, str):
            result.append(strings.pop(0))

    return result