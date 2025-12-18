"""
QUESTION:
Develop a function called `find_max_value` that takes a list of mixed data types as input and returns the maximum numerical value (including integers and floats) within the list. The list may contain nested lists to any arbitrary level, as well as string representations of numbers. The function should convert these strings to numerical values for comparison and handle potential exceptions without breaking the program. If the list contains no numerical values, the function should return `None`.
"""

def find_max_value(input_list):
    max_val = None
    for element in input_list:
        if isinstance(element, list):
            max_val_sublist = find_max_value(element)
            if max_val is None or (max_val_sublist is not None and max_val_sublist > max_val):
                max_val = max_val_sublist
        else:
            try:
                num = float(element)
                if max_val is None or num > max_val:
                    max_val = num
            except (ValueError, TypeError):  
                continue
    return max_val