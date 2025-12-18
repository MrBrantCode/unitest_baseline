"""
QUESTION:
Implement a function `convert_data(data, data_type)` that takes in a piece of data and its corresponding data type, and returns the converted data based on the provided mapping. The mapping includes 'int8': int, 'int16': int, 'int32': int, 'int64': int, 'uint8': int, 'uint16': int, 'uint32': int, 'uint64': int, 'float32': float, 'float64': float, and 'string': str. You also need to determine the appropriate Python data type for 'time' and add it to the mapping. The function should return "Unsupported data type" if the data type is not found in the mapping.
"""

from datetime import datetime

def convert_data(data, data_type):
    data_type_mapping = {
        'int8': int,
        'int16': int,
        'int32': int,
        'int64': int,
        'uint8': int,
        'uint16': int,
        'uint32': int,
        'uint64': int,
        'float32': float,
        'float64': float,
        'string': str,
        'time': datetime.fromisoformat
    }

    if data_type in data_type_mapping:
        return data_type_mapping[data_type](data)
    else:
        return "Unsupported data type"