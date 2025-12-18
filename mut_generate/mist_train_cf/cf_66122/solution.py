"""
QUESTION:
Create a function named `enhance_func` that takes a list of elements as input, appends '5' to the string conversion of each integer in the list, and returns a new list containing these modified integers. The function should handle non-integer items, empty lists, and large input sizes efficiently. It should not raise exceptions for non-integer items, but instead skip them and continue processing the rest of the list. The function should have a time complexity of O(n) and space complexity of O(n), where n is the number of items in the list.
"""

def enhance_func(lst):
    if not lst:
        return []

    result = []

    for element in lst:
        if not isinstance(element, int):
            continue
        result.append(int(str(element) + '5'))

    return result