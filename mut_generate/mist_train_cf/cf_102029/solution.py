"""
QUESTION:
Combine two given lists of strings into a list with unique strings, ignoring case sensitivity. Write a function `combine_unique_strings` that takes two lists of strings as input and returns a list containing all unique strings from both lists, without any duplicates.
"""

def combine_unique_strings(list1, list2):
    """
    Combine two given lists of strings into a list with unique strings, ignoring case sensitivity.

    Args:
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        list: A list containing all unique strings from both lists, without any duplicates.
    """
    # Convert both lists to lowercase to handle case-insensitive duplicates
    list1 = [x.lower() for x in list1]
    list2 = [x.lower() for x in list2]

    # Combine the lists and convert to a set to remove duplicates
    combined_set = set(list1 + list2)

    # Convert the set back to a list and restore the original casing
    combined_list = [x.capitalize() for x in combined_set]

    return combined_list