"""
QUESTION:
Write a function `assign_value` that takes a nested list or dictionary as input. For each element in the input, assign the value 0 if it is an empty string, NaN, or a negative number, and assign the value 1 if it is a positive even number. Leave other values unchanged. The function should handle nested lists and dictionaries recursively.
"""

def assign_value(nested_data):
    if isinstance(nested_data, list):  
        return [assign_value(item) for item in nested_data]  
    elif isinstance(nested_data, dict):  
        return {key: assign_value(value) for key, value in nested_data.items()}  
    elif isinstance(nested_data, str) and nested_data == '':  
        return 0
    elif isinstance(nested_data, float) and math.isnan(nested_data):  
        return 0
    elif isinstance(nested_data, int) and nested_data < 0:  
        return 0
    elif isinstance(nested_data, int) and nested_data > 0 and nested_data % 2 == 0:  
        return 1
    else:
        return nested_data  