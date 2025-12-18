"""
QUESTION:
Create a function `convert_data_types` that takes a dictionary as input and returns a list of tuples, where each tuple contains a key from the dictionary and the corresponding data type of its value. The data type should be determined after attempting to convert the value to an integer if it consists of only digits, or to a float if the integer conversion fails. If both conversions fail, the data type should be that of the original value.
"""

def convert_data_types(nested_dict):
    output = []
    for key, value in nested_dict.items():
        if isinstance(value, str) and value.isdigit():
            value = int(value)
        elif isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                pass
        data_type = type(value)
        output.append((key, data_type))
    return output