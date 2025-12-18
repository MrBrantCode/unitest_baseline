"""
QUESTION:
Write a function named `sum_nested_dict_values` that takes a dictionary as input. The dictionary may contain integers, lists, sets, tuples, and nested dictionaries as values. If a value is an integer, add it to the sum. If a value is a tuple, square each element and add the squared values to the sum. If a value is a list or a set, square each element, remove duplicates, and add the unique squared values to the sum. If a value is a dictionary, recursively apply these rules. Return the total sum of all values in the dictionary.
"""

def sum_nested_dict_values(nested_dict):
    total_sum = 0

    for key, value in nested_dict.items():
        if isinstance(value, int):
            total_sum += value
        elif isinstance(value, tuple):
            for num in value:
                total_sum += num ** 2
        elif isinstance(value, list) or isinstance(value, set):
            unique_squared_values = set()
            for num in value:
                unique_squared_values.add(num ** 2)
            total_sum += sum(unique_squared_values)
        elif isinstance(value, dict):
            total_sum += sum_nested_dict_values(value)

    return total_sum