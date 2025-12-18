"""
QUESTION:
Create a function named `compare_lists` that takes two lists, `input_list` and `predefined_list`, as input. The function should return a new list containing the elements that are present in both `input_list` and `predefined_list`, with the comparison being case-insensitive. The resulting list should not contain any duplicate elements. The input lists should not exceed a length of 1000.
"""

def compare_lists(input_list, predefined_list):
    # Convert both lists to lowercase
    input_list = [item.lower() for item in input_list]
    predefined_list = [item.lower() for item in predefined_list]

    # Find common elements and remove duplicates
    common_elements = list(set(input_list) & set(predefined_list))

    return common_elements