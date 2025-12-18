"""
QUESTION:
Implement the `truncate_list` function to truncate a given list to a specified maximum length. The function should take two parameters: `input_list` and `max_length`, where `input_list` is the list to be truncated and `max_length` is the maximum allowed length. If the length of `input_list` exceeds `max_length`, the function should return a new list containing only the first `max_length` elements of `input_list`.
"""

def truncate_list(input_list, max_length):
    """
    Truncates a given list to a specified maximum length.

    Args:
        input_list (list): The list to be truncated.
        max_length (int): The maximum allowed length.

    Returns:
        list: A new list containing only the first max_length elements of input_list.
    """
    if len(input_list) > max_length:
        return input_list[:max_length]
    else:
        return input_list