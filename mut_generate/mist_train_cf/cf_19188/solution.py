"""
QUESTION:
Write a function named `find_common_items` that takes two lists as input, `list1` and `list2`, and returns a new list containing the common items between the two lists. The function should handle lists of any length and the items in the lists can be of any data type, including nested lists, which should be flattened before comparison.
"""

def find_common_items(list1, list2):
    """
    This function takes two lists as input and returns a new list containing the common items between the two lists.
    
    The function handles lists of any length and the items in the lists can be of any data type, including nested lists, 
    which are flattened before comparison.

    Args:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Returns:
        list: A new list containing the common items between the two input lists.
    """

    def flatten_list(lst):
        """Helper function to flatten a nested list."""
        flattened_list = []
        for item in lst:
            if isinstance(item, list):
                flattened_list.extend(flatten_list(item))
            else:
                flattened_list.append(item)
        return flattened_list

    # Flatten the input lists
    list1 = flatten_list(list1)
    list2 = flatten_list(list2)

    # Use set intersection to find common items
    common_items = list(set(list1) & set(list2))

    return common_items