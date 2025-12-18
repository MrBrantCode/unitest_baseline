"""
QUESTION:
Write a function `sum_numbers_in_structure` that takes a nested data structure as input and returns the sum of all numerical values (integers and floats) it contains, regardless of their depth within the structure. The input data structure can be a dictionary or a list, and it may contain additional nested dictionaries and lists. If the input value is not a dictionary or a list, it should be treated as a single value (if numerical) or ignored (if non-numerical).
"""

def sum_numbers_in_structure(structure):
    if isinstance(structure, dict):
        return sum(sum_numbers_in_structure(val) for val in structure.values())
    elif isinstance(structure, list):
        return sum(sum_numbers_in_structure(val) for val in structure)
    elif isinstance(structure, (int, float)):
        return structure
    else:
        return 0