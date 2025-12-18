"""
QUESTION:
Create a function called `find_none` that takes a tuple of variable length and data type as input. The function should return the index of the first occurrence of `None` in the tuple, along with the total count of `None` values. If no `None` value is found, the function should return the message "No None values found".
"""

def find_none(input_tuple):
    none_count = 0
    none_index = None
    for idx, value in enumerate(input_tuple):
        if value is None:
            none_count += 1
            if none_index is None:
                none_index = idx
    if none_count == 0:
        return "No None values found"
    else:
        return none_index, none_count