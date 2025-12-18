"""
QUESTION:
Create a function named `create_dict` that takes two lists of the same length, `list1` and `list2`, as input. The function should return a dictionary where the keys are obtained by converting the elements of `list1` to uppercase and adding a suffix of "KEY", and the values are obtained by converting the elements of `list2` to integers and adding 10 to each value. The dictionary should only contain unique keys, and it should be sorted in descending order based on the values.
"""

def create_dict(list1, list2):
    """
    Create a dictionary from two lists of the same length.

    The keys of the dictionary are obtained by converting the elements of list1 to uppercase and adding a suffix of "KEY".
    The values are obtained by converting the elements of list2 to integers and adding 10 to each value.
    The dictionary only contains unique keys and is sorted in descending order based on the values.

    Args:
        list1 (list): The list of strings used to create the keys.
        list2 (list): The list of strings used to create the values.

    Returns:
        dict: A dictionary with the specified keys and values.
    """
    my_dict = {}
    for i in range(len(list1)):
        key = list1[i].upper() + "KEY"
        value = int(list2[i]) + 10
        my_dict[key] = value

    return {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}