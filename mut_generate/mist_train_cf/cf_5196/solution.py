"""
QUESTION:
Combine two lists into a single list without duplication and in alphabetical order, without using any built-in sorting or deduplication functions. Implement a function named `combine_lists` that takes two lists as input, `list_one` and `list_two`, and returns the combined list.
"""

def combine_lists(list_one, list_two):
    """
    Combines two lists into a single list without duplication and in alphabetical order.

    Args:
        list_one (list): The first list to combine.
        list_two (list): The second list to combine.

    Returns:
        list: The combined list without duplicates in alphabetical order.
    """

    # Create an empty list to store the combined and sorted elements
    combined_list = []

    # Combine elements from list_one, avoiding duplicates
    for element in list_one:
        if element not in combined_list:
            combined_list.append(element)

    # Combine elements from list_two, avoiding duplicates
    for element in list_two:
        if element not in combined_list:
            combined_list.append(element)

    # Sort combined_list using a simple bubble sort for demonstration purposes
    n = len(combined_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if combined_list[j] > combined_list[j + 1]:
                combined_list[j], combined_list[j + 1] = combined_list[j + 1], combined_list[j]

    return combined_list