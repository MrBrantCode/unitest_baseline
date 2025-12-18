"""
QUESTION:
Design a function named `process_list` that takes a list of integers as input and returns a reversed version of the sorted list. If the input list is not sorted in ascending order, the function should first sort it before inverting it. The function should handle edge cases such as an empty list or a list with a single element.
"""

def process_list(input_list):
    """
    This function takes list as input, checks if that list is sorted, if not sorts that list, and finally inverts the list.

    :param input_list: List of integers
    :return: Inverted version of sorted list
    """
    # Check if the list is sorted in ascending order
    if input_list != sorted(input_list):
        # If not sorted, sort the list
        input_list.sort()

    # Invert the list
    input_list = input_list[::-1]

    return input_list