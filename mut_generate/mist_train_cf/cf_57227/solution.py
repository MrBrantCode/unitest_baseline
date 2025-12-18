"""
QUESTION:
Create a function `transform_dictionary` that takes a dictionary `data` and a list of integers `indices` as parameters. The dictionary `data` contains keys representing unique IDs and values as lists of diverse data attributes. The function should return a new dictionary with the same keys, but the values should be lists containing only the elements at the specified index positions from the original lists. Ensure that the function handles cases where the index is out of range for a given list.
"""

def transform_dictionary(data, indices):
    transformed_dict = {}
    for id, record in data.items():
        new_record = [record[i] for i in indices if i < len(record)]
        transformed_dict[id] = new_record
    return transformed_dict