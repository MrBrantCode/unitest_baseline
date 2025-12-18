"""
QUESTION:
Generate a function called `get_data_type_and_size` that takes a list of elements as input. For each element, return its data type and size in bytes if the element is an integer or floating-point number, and only its data type if the element is not an integer or floating-point number. The size of an element is determined by its actual memory usage.
"""

def get_data_type_and_size(lst):
    result = []
    for element in lst:
        if isinstance(element, (int, float)):
            result.append(f"{element}: {type(element).__name__}, {element.__sizeof__()} bytes")
        else:
            result.append(f"{element}: {type(element).__name__}")
    return result