"""
QUESTION:
Write a function `get_dictionaries_with_key_value_pair` that takes a list of dictionaries `dict_list`, a key, and a value as input. The function should return a new list of dictionaries that contain the specified key-value pair using dictionary comprehension.
"""

def get_dictionaries_with_key_value_pair(dict_list, key, value):
    return [d for d in dict_list if d.get(key) == value]