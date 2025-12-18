"""
QUESTION:
Write a function `group_list_elements` that takes a list and an integer as inputs and returns a list of sublists. The original list must have a length that is a multiple of 8 and the sublist length must be a multiple of 3. The function should divide the original list into sublists of the specified length.
"""

def group_list_elements(lst, sublist_length):
    """
    Divide a list into sublists of a specified length.

    Args:
        lst (list): The original list. Its length must be a multiple of 8.
        sublist_length (int): The length of the sublists. It must be a multiple of 3.

    Returns:
        list: A list of sublists.

    Raises:
        AssertionError: If the original list length is not a multiple of 8 or the sublist length is not a multiple of 3.
    """
    assert len(lst) % 8 == 0, "Original list length is not a multiple of 8"
    assert sublist_length % 3 == 0, "Sublist length is not a multiple of 3"

    return [lst[i:i+sublist_length] for i in range(0, len(lst), sublist_length)]