"""
QUESTION:
Create a function called `generate_dicts` that generates a sequence of N vacant dictionaries. The function should take an integer `n` as input and return a dictionary with `n` key-value pairs, where each key is a unique identifier in the format 'dict_i' and each value is an empty dictionary. The function should ensure the uniqueness of each identifier and the emptiness of the nested dictionaries.
"""

def generate_dicts(n):
    return {f'dict_{i}': {} for i in range(n)}