"""
QUESTION:
Write a function `assign_zero(data)` that takes an input data which can be a list or a dictionary, and returns the modified data where all empty strings and NaN values are replaced with 0. The function should handle nested lists and dictionaries recursively.
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