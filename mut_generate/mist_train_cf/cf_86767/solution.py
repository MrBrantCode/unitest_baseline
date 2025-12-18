"""
QUESTION:
Write a function named combine_lists that combines two given lists of strings while ensuring that the resulting list does not contain any duplicates, with case-insensitive comparison and preserving the original casing. The function should be able to handle lists of any size.
"""

def combine_lists(list1, list2):
    """
    Combine two lists of strings, removing duplicates with case-insensitive comparison.

    Args:
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        list: A list of unique strings from both input lists.
    """
    seen = set()
    combined_list = []
    for item in list1 + list2:
        lower_item = item.lower()
        if lower_item not in seen:
            combined_list.append(item)
            seen.add(lower_item)
    return combined_list