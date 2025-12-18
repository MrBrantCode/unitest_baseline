"""
QUESTION:
Design a function named `nested_dict` that takes a set of numeric values as input and returns a nested dictionary where each numeric value from the set is used as a key in a sequential, nested key-value structure. The function should recursively create the nested dictionary until all elements from the input set have been used. The input set may be empty.
"""

def nested_dict(set_values):
    if len(set_values) == 0:  
        return {}
    else:
        key_value = set_values.pop()  
        return {key_value: nested_dict(set_values)}