"""
QUESTION:
Write a function `sum_dict_values` that takes a dictionary as an argument, recursively adds all numerical values present in it, and handles nested dictionaries. The function should exclude non-numerical values from the addition and handle various data types.
"""

def sum_dict_values(d):
    total = 0
    for k, v in d.items():
        if isinstance(v, dict):   
            total += sum_dict_values(v)    
        elif isinstance(v, (int, float, complex)):   
            total += v
    return total