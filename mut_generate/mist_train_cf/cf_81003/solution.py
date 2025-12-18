"""
QUESTION:
Write a function named `frequency_counter` that accepts a list of numeric values and returns a dictionary depicting the occurrence frequency of each distinct numeric element, ignoring non-numeric entries. The function should not crash on an empty list.
"""

def frequency_counter(lst):
    result = {}
    for i in lst:
        if isinstance(i, (int, float)):
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
    return result