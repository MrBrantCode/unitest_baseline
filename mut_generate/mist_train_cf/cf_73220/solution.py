"""
QUESTION:
Design a Python function `remove_duplicates` that takes a list of elements as input and returns a new list with all duplicate elements removed, while preserving the original order of the remaining elements. The function should not use any built-in functions that remove duplicates or sort the list.
"""

def remove_duplicates(elements_list):
    result = []
    for element in elements_list:
        if element not in result:
            result.append(element)
    return result