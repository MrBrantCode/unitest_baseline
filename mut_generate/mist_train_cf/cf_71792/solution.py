"""
QUESTION:
Create a function `create_ordered_dict` that takes three parameters: a string `text`, a string `delimiter`, and a list `collection`. The function should return an ordered dictionary where each key is created by concatenating `text`, `delimiter`, and an incrementing integer starting from 1, and each value is created by concatenating the corresponding key and the element from the list at the same index, separated by a comma and a space. The function should only use the standard Python library and should have a linear time complexity with respect to the size of the input list.
"""

from collections import OrderedDict

def create_ordered_dict(text, delimiter, collection):
    dict_result = OrderedDict()
    for i, element in enumerate(collection, start=1):
        key = f"{text}{delimiter}{i}"
        value = f"{key}, {element}"
        dict_result[key] = value
    return dict_result