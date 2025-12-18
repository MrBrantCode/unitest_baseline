"""
QUESTION:
Create a function `common_elements(num_list, comparison_list)` that takes two lists of numbers as input, generates a new list where each number in `num_list` is doubled and multiplied by its index, and returns a third list of common elements between the new list and `comparison_list` in ascending order. The function should handle cases where the input lists are empty or contain non-numeric elements.
"""

def common_elements(num_list, comparison_list):
    # check if lists are empty or not
    if not num_list or not comparison_list:
        return 'Input lists cannot be empty'

    # check if lists contain only numbers
    if not all(isinstance(i, int) or isinstance(i, float) for i in num_list+comparison_list):
        return 'Input lists should contain numbers only'

    # double each number and multiply by its index in num_list
    num_list_doubled = [i*2*j for j, i in enumerate(num_list)]

    # find common elements, make it list of unique elements and sort in ascending order
    common = sorted(list(set(num_list_doubled) & set(comparison_list)))

    return common