"""
QUESTION:
Create a function `sort_dict` that takes a dictionary as an input and returns a new dictionary sorted by its values. The function should sort numeric values (int and float) in ascending order and string values alphabetically. The function must handle dictionaries with mixed data types as values.
"""

def sort_dict(d):
    numeric_items = {k: v for k, v in d.items() if isinstance(v, (int, float))}
    str_items = {k: v for k, v in d.items() if isinstance(v, str)}
    sorted_dict = {k: v for k, v in sorted(numeric_items.items(), key=lambda item: item[1])}
    sorted_dict.update({k: v for k, v in sorted(str_items.items(), key=lambda item: item[1])})
    return sorted_dict