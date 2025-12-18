"""
QUESTION:
Write a function `process_data(an_dict)` that takes a dictionary as input and returns a tuple containing the sum of all numerical values and the concatenation of all string values in reverse order of their appearance in the dictionary. The function should handle both integers and floats as numerical values.
"""

def process_data(an_dict):
    key_order = list(an_dict.keys())[::-1]
    sum_num = 0
    concat_str = ""
    for key in key_order:
        data = an_dict[key]
        if isinstance(data, str):
            concat_str += data
        elif isinstance(data, (int, float)):
            sum_num += data
    return (sum_num, concat_str)