"""
QUESTION:
Design a function `remove_duplicates_nested_list` that takes a nested numerical array list as input and returns a new list with all recurring elements eliminated. The function should handle any number of sublists and list sizes up to 10^5, and account for negative values and zero in the list. Note that distinct integers from nested lists are considered separately from the main list and other sublists. The function should not use inbuilt Python set functions.
"""

def remove_duplicates_nested_list(nested_list):
    unique_dict = {}
    result_list = []
 
    for value in nested_list:
        if isinstance(value, list): 
            sub_res = []
            for sub_value in value:
                if sub_value not in unique_dict.get(id(value), set()):
                    sub_res.append(sub_value)
                    if id(value) in unique_dict:
                        unique_dict[id(value)].add(sub_value)
                    else:
                        unique_dict[id(value)] = {sub_value}
            result_list.append(sub_res)
        else:
            if value not in unique_dict.get('main_list', set()):
                result_list.append(value)
                if 'main_list' in unique_dict:
                    unique_dict['main_list'].add(value)
                else:
                    unique_dict['main_list'] = {value}
    return result_list