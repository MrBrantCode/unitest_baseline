"""
QUESTION:
Implement a function `dataset_to_array` that takes a list of dictionaries as input, where each dictionary represents a data point with key-value pairs of attributes and values. The function should return a 2D array where each row represents a data point and each column represents an attribute. The attribute order in the output should be consistent across all rows. The function should handle empty input and return an empty list in that case.
"""

def dataset_to_array(data: list) -> list:
    if not data:
        return []

    attributes = list(data[0].keys())
    result = [[entry[attr] for attr in attributes] for entry in data]

    return result