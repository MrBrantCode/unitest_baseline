"""
QUESTION:
Create a function `fetch_max` that takes a dictionary `d` as input where the values can be either integers or strings. The function should return the maximum value from the dictionary. If the maximum value is a string, it should be the string with the greatest lexicographical order. The function should be able to handle dictionaries with mixed value types and return the maximum value based on the following rules: 

- If both integer and string values are present, compare the maximum string value with the string representation of the maximum integer value and return the greater one.
- If only string values are present, return the maximum string value.
- If only integer values are present, return the maximum integer value.

The function should not assume that all dictionary values are of the same data type.
"""

def fetch_max(d):
    values = list(d.values())
    str_values = [val for val in values if isinstance(val, str)]
    int_values = [val for val in values if isinstance(val, int)]
    
    max_str_value = max(str_values) if str_values else None
    max_int_value = max(int_values) if int_values else None
    
    if max_str_value is not None and max_int_value is not None:
        return max_str_value if max_str_value > str(max_int_value) else max_int_value
    elif max_str_value is not None:
        return max_str_value
    else:
        return max_int_value