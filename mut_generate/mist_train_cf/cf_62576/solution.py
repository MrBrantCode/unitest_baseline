"""
QUESTION:
Write a function `sum_values(data)` that calculates the sum of all integer values in a given multi-level dictionary `data`. The dictionary may contain other dictionaries and lists as values. The function should recursively traverse the dictionary and its nested structures to find and sum up all integer values.
"""

def sum_values(data):
    total = 0
    if type(data) == dict:
        for key, value in data.items():
            if type(value) in (dict, list):
                total += sum_values(value)
            if type(value) == int:
                total += value
    if type(data) == list:
        for item in data:
            if type(item) in (dict, list):
                total += sum_values(item)
            if type(item) == int:
                total += item
    return total