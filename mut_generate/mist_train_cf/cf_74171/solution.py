"""
QUESTION:
Create a function called `create_registry` that takes a list as input and returns a list of dictionaries. Each dictionary should contain the index, data type (as a string), and length (if the item is a string) of each element in the input list. The function should be able to handle nested lists.
"""

def create_registry(input_list):
    registry = []

    for index, item in enumerate(input_list):
        data_type = type(item)

        if data_type == str:
            length = len(item)
        elif data_type == list:
            length = len(item)
        else:
            length = None

        registry.append({'index': index, 'datatype': data_type.__name__, 'length': length})

    return registry