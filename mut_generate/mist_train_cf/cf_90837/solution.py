"""
QUESTION:
Create a function `assign_zero` that takes in a value that can be a list, dictionary, or any other type, and returns the same structure with all empty strings and NaN values replaced with 0. The function should handle nested lists and dictionaries.
"""

def assign_zero(data):
    if isinstance(data, list):
        for i in range(len(data)):
            data[i] = assign_zero(data[i])
        return data
    elif isinstance(data, dict):
        for key in data:
            data[key] = assign_zero(data[key])
        return data
    elif data == '' or data != data:  # check for empty string or NaN
        return 0
    else:
        return data