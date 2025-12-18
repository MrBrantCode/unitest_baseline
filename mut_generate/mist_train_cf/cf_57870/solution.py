"""
QUESTION:
Create a function named `merge_and_remove_duplicates` that merges elements from three input lists into a single string while maintaining the original order. The function should remove any duplicate words from the final string and return the resulting string. Each input list can contain any number of elements.
"""

def merge_and_remove_duplicates(list1, list2, list3):
    """
    Merges elements from three input lists into a single string while maintaining the original order.
    Removes any duplicate words from the final string.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.
        list3 (list): The third input list.

    Returns:
        str: The merged string with no duplicates.
    """
    # Merging the lists
    merged_list = list1 + list2 + list3

    # Removing duplicates by converting the list to a dict, then back to a list
    no_duplicates_list = list(dict.fromkeys(merged_list))

    # Converting the list to a single string
    return ' '.join(no_duplicates_list)