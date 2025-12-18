"""
QUESTION:
Implement a function `filter_instances` that takes a nested data structure and a class as input, and returns a new data structure with all instances of the specified class and its subclasses removed. The function should handle nested lists, tuples, and sets, and remove any containers that contain instances of the specified class. If an instance of the specified class is found at the top level of the data structure, it should be removed as well. The function should have the following signature: `def filter_instances(data_structure, class_to_filter):`
"""

def filter_instances(data_structure, class_to_filter):
    if isinstance(data_structure, class_to_filter):
        return None
    elif isinstance(data_structure, (list, tuple, set)):
        filtered = []
        for item in data_structure:
            result = filter_instances(item, class_to_filter)
            if result is not None:
                filtered.append(result)
        return type(data_structure)(filtered)
    else:
        return data_structure