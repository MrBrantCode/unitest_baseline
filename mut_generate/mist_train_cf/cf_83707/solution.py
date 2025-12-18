"""
QUESTION:
Construct a function `multiply_corresponding_elements` that takes two lists, `list_one` and `list_two`, as input and returns a new list. The new list should contain elements that are the product of corresponding values from `list_one` and `list_two`, along with their index position in `list_one`. If `list_two` is missing an element at a particular index, use 2 as the default multiplier. The function should be able to handle lists of different lengths.
"""

def multiply_corresponding_elements(list_one, list_two):
    """
    This function multiplies corresponding elements from two lists.
    If list_two is missing an element at a particular index, it uses 2 as the default multiplier.

    Args:
        list_one (list): The primary list of numbers.
        list_two (list): The secondary list of numbers.

    Returns:
        list: A new list containing the products of corresponding elements from list_one and list_two.
    """
    return [list_one[i]*list_two[i] if i < len(list_two) else list_one[i]*2 for i in range(len(list_one))]