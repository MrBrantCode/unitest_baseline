"""
QUESTION:
Create a function `extract_values` that takes a dictionary `d` as input, extracts its unique values, and returns them as a list. The function should be able to process both contiguous data and non-contiguous data. If the input dictionary has nested dictionaries, the function should flatten these nested dictionaries and consider their values as unique values of the original dictionary.
"""

def extract_values(d):
    """
    Extracts unique values from a dictionary, including those in nested dictionaries.

    Args:
        d (dict): The dictionary to extract values from.

    Returns:
        list: A list of unique values in the dictionary.
    """
    values = set()
    for key, value in d.items():
        if isinstance(value, dict):
            values.update(extract_values(value))
        else:
            values.add(value)
    return list(values)