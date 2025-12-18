"""
QUESTION:
Write a function named `compare_lists` that takes two lists `input_list` and `predefined_list` as input, each containing up to 1000 string elements. The function should return a new list containing only the elements that are present in both lists, with the comparison performed case-insensitively, and any duplicate elements removed.
"""

def compare_lists(input_list, predefined_list):
    # Convert both lists to lowercase
    input_list = [item.lower() for item in input_list]
    predefined_list = [item.lower() for item in predefined_list]

    # Find common elements and remove duplicates
    common_elements = list(set(input_list) & set(predefined_list))

    return common_elements