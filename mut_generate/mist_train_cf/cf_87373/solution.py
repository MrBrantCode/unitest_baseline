"""
QUESTION:
Write a function `find_common_items` that takes two lists as input and returns a list of their common items, excluding duplicates. The function should handle nested lists by flattening them and considering their elements as part of the original list. It should also handle lists with dictionaries as elements by considering the keys and values of the dictionaries as separate elements in the comparison. The input lists can contain integers, floating-point numbers, and strings, and have a maximum length of 1000.
"""

def find_common_items(list1, list2):
    def flatten_list(lst):
        flattened_list = []
        for item in lst:
            if isinstance(item, list):
                flattened_list.extend(flatten_list(item))
            else:
                flattened_list.append(item)
        return flattened_list


    def convert_dict_to_list(lst):
        converted_list = []
        for item in lst:
            if isinstance(item, dict):
                converted_list.extend(list(item.keys()))
                converted_list.extend(list(item.values()))
            else:
                converted_list.append(item)
        return converted_list


    def remove_duplicates(lst):
        return list(set(lst))


    # Flatten the nested lists
    flattened_list1 = flatten_list(list1)
    flattened_list2 = flatten_list(list2)
    
    # Convert dictionaries to a list of their keys and values
    flattened_list1 = convert_dict_to_list(flattened_list1)
    flattened_list2 = convert_dict_to_list(flattened_list2)
    
    # Find the common items between the lists
    common_items = list(set(flattened_list1) & set(flattened_list2))
    
    # Remove any duplicate common items
    common_items = remove_duplicates(common_items)
    
    return common_items