"""
QUESTION:
Create a function `combine_lists` that takes two lists, `list1` and `list2`, as input. The function should return a dictionary where the keys are the elements from `list1` that are in uppercase letters only and the values are the corresponding elements from `list2` that are divisible by 2. The resulting dictionary should only include key-value pairs where both conditions are met.
"""

def combine_lists(list1, list2):
    """
    This function combines two lists into a dictionary where the keys are the 
    elements from list1 that are in uppercase letters only and the values are 
    the corresponding elements from list2 that are divisible by 2.

    Args:
        list1 (list): The list containing the keys for the dictionary.
        list2 (list): The list containing the values for the dictionary.

    Returns:
        dict: A dictionary with the combined key-value pairs.
    """
    return {k: v for k, v in zip(list1, list2) if k.isupper() and v % 2 == 0}