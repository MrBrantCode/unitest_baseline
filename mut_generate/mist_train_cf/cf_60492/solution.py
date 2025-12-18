"""
QUESTION:
Design a function `functionX` that accepts a single argument `data` of any data type and returns the data type of the input. The function should also be capable of throwing a custom exception when the passed argument is of a specific, user-defined data type.
"""

def functionX(data, exception_type=None):
    if exception_type and isinstance(data, exception_type):
        raise Exception(f"Custom exception: data is of type {str(exception_type)}")

    if not isinstance(data, str):
        data = str(data)

    return type(data)