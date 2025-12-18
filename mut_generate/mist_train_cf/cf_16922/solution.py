"""
QUESTION:
Write a function named `extract_values` that takes in a list of dictionaries `dictionaries`, a list of excluded keys `excluded_keys`, and an operation `operation` to be performed on the extracted values. 

The function should recursively extract all values from the list of dictionaries, excluding the specified keys and handling nested dictionaries. The extracted values should be stored in the same order as they appear in the list of dictionaries. 

The function should also handle different data types, missing keys, and null values. The operation to be performed on the extracted values should be configurable and can be different for different values. 

The function should return the list of extracted values after applying the specified operation. The default operation should be an identity function that returns the value itself. The excluded keys should default to an empty list if not provided. 

Optimize the function for efficiency, especially for large lists of dictionaries or computationally expensive operations.
"""

from collections import OrderedDict

def extract_values(dictionaries, excluded_keys=None, operation=None):
    if excluded_keys is None:
        excluded_keys = []
    if operation is None:
        operation = lambda x: x

    extracted_values = []
    for dictionary in dictionaries:
        extracted_values.extend(_extract_values_recursive(dictionary, excluded_keys, operation))
    
    return extracted_values

def _extract_values_recursive(dictionary, excluded_keys, operation):
    values = []
    for key, value in dictionary.items():
        if key not in excluded_keys:
            if isinstance(value, dict):
                values.extend(_extract_values_recursive(value, excluded_keys, operation))
            else:
                value = operation(value)
                values.append(value)
    return values