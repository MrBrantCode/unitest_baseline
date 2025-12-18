"""
QUESTION:
Write a function `sum_nested_values` that calculates the sum of all values in a nested dictionary. The dictionary can contain integers, floats, lists, sets, and tuples as values. If a value is a tuple, each element within the tuple should be squared before being added to the sum. The function should recursively handle nested dictionaries.
"""

def sum_nested_values(data):
    total_sum = 0

    for value in data.values():
        if isinstance(value, dict):
            total_sum += sum_nested_values(value)
        elif isinstance(value, (int, float)):
            total_sum += value
        elif isinstance(value, (list, set, tuple)):
            for element in value:
                if isinstance(element, (list, set, tuple)):
                    if isinstance(element, tuple):
                        for num in element:
                            total_sum += num**2
                    else:
                        for num in element:
                            total_sum += num
                elif isinstance(element, dict):
                    total_sum += sum_nested_values(element)
                else:
                    total_sum += element

    return total_sum