"""
QUESTION:
Write a function `analyze_data` that takes a list as input, recursively iterates over the elements, and returns the integers, single-character strings, dictionaries, and other elements in the list, along with their counts. The function should sort the integers and single-character strings in ascending order and be able to handle nested lists and an arbitrary number of elements. The function should have a time complexity of O(n).
"""

def analyze_data(input_list):
    integers = []
    chars = []
    dicts = []
    other = []
    for item in input_list:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str) and len(item) == 1:
            chars.append(item)
        elif isinstance(item, dict):
            dicts.append(item)
        elif isinstance(item, list):
            # Recursively call function for nested lists
            nested_integers, nested_chars, nested_dicts, nested_other = analyze_data(item)
            integers.extend(nested_integers)
            chars.extend(nested_chars)
            dicts.extend(nested_dicts)
            other.extend(nested_other)
        else:
            other.append(item)
    integers.sort()
    chars.sort()
    return integers, chars, dicts, other