"""
QUESTION:
Write a function named `iterate_dict` that takes a nested dictionary `d` as input and returns the sum of all its values. The function should be able to handle dictionaries of arbitrary depth.
"""

def iterate_dict(d):
    result = 0
    for value in d.values():
        if type(value) is dict:
            result += iterate_dict(value)
        else:
            result += value
    return result