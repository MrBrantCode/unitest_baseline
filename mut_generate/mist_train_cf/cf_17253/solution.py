"""
QUESTION:
Create a function named `create_dict_from_lists` that combines two input lists into a dictionary. The function should only include elements from the first list (`list1`) that have corresponding elements in the second list (`list2`) at the same index, and the corresponding elements in `list2` must be divisible by 2.
"""

def create_dict_from_lists(list1, list2):
    """
    This function combines two input lists into a dictionary.
    It only includes elements from the first list that have corresponding elements in the second list at the same index,
    and the corresponding elements in the second list must be divisible by 2.

    Args:
        list1 (list): The list of keys for the dictionary.
        list2 (list): The list of values for the dictionary.

    Returns:
        dict: A dictionary created from the input lists.
    """
    dictionary = {}
    for i in range(min(len(list1), len(list2))):
        if list2[i] % 2 == 0:
            dictionary[list1[i]] = list2[i]
    return dictionary