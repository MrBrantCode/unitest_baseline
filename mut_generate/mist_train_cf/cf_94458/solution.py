"""
QUESTION:
Create a function `extract_values` that takes a list of dictionaries, a list of excluded keys, and a function to perform an operation on each extracted value. The function should:

- Extract all values from the list of dictionaries, excluding the specified keys.
- Handle nested dictionaries by recursively extracting their values.
- Apply the given operation to each extracted value.
- Maintain the order of extracted values.
- Handle different data types and missing keys/null values.
- Optimize performance for large lists of dictionaries or computationally expensive operations.

The function should return a list of extracted values after applying the specified operation.
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