"""
QUESTION:
Create a function named `find_elements_in_mixed_data_type_list` that takes a nested list containing mixed data types (including integers, strings, sub-lists, tuples, and dictionaries) as input. The function should return two dictionaries: one containing the count of each data type in the list, and another containing the indices of these elements in the list. The function should not recursively traverse nested data structures.
"""

def find_elements_in_mixed_data_type_list(list_obj):
    count_dict = {}
    indices_dict = {}

    # Enumerate through every elements in list
    for index, value in enumerate(list_obj):
        type_key = type(value).__name__

        # Add count and index in the dictionaries
        if type_key in count_dict:
            count_dict[type_key] += 1
            indices_dict[type_key].append(index)
        else:
            count_dict[type_key] = 1
            indices_dict[type_key] = [index]

    return count_dict, indices_dict