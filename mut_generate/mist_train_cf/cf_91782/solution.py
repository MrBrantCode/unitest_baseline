"""
QUESTION:
Write a function called `merge_lists` that takes two lists `list_a` and `list_b` as input. The function should return a new list containing unique elements from both input lists. It should include only elements from `list_a` that are greater than 2 and elements from `list_b` that are less than 5.
"""

def merge_lists(list_a, list_b):
    """
    Merge two lists and return a new list containing unique elements from both input lists.
    The new list includes only elements from list_a that are greater than 2 and elements from list_b that are less than 5.

    Args:
        list_a (list): The first input list.
        list_b (list): The second input list.

    Returns:
        list: A new list containing unique elements from both input lists.
    """
    merged_list = list(set(list_a + list_b))  # Merge the two lists and remove duplicates
    
    return [item for item in merged_list if (item > 2 and item in list_a) or (item < 5 and item in list_b)]