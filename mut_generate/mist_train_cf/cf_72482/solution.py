"""
QUESTION:
Create a function `traverse_dict(data)` that takes a multi-layered dictionary as input, where the dictionary can contain nested arrays and strings with numerical values. The function should recursively traverse the dictionary and return the sum of all numeric values within it. The function should handle integers, strings that can be converted to integers, and nested lists and dictionaries.
"""

def traverse_dict(data):
    aggregate = 0
    if type(data) is dict:
        for key in data:
            aggregate += traverse_dict(data[key])
    elif type(data) is list:
        for i in data:
            aggregate += traverse_dict(i)
    elif type(data) is str:
        if data.isdigit():
            aggregate += int(data)
    elif type(data) is int:
        aggregate += data

    return aggregate