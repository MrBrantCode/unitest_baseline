"""
QUESTION:
Create a function named `compare_lists` that takes two lists of strings as input. The function should return a new list containing only the elements that are present in both input lists, with the comparison being case-insensitive. The returned list should contain the elements in lowercase.
"""

def compare_lists(my_list, pre_defined_list):
    my_list_lower = [element.lower() for element in my_list]
    pre_defined_list_lower = [element.lower() for element in pre_defined_list]
    common_elements = [element for element in my_list_lower if element in pre_defined_list_lower]
    return common_elements