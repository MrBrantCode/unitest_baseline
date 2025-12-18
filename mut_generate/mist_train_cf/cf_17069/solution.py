"""
QUESTION:
Write a function `combine_and_sort_lists` that takes two lists as input and returns a new list where each element is a tuple containing one element from each input list, in the order they appear. Exclude any values from the first list that are divisible by 3 and sort the resulting list in descending order based on the sum of each pair of values.
"""

def combine_and_sort_lists(list1, list2):
    """
    Combine two lists by index, excluding values from list1 that are divisible by 3,
    and sort the resulting list in descending order based on the sum of each pair of values.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A new list where each element is a tuple containing one element from each input list.
    """
    return sorted([(x, y) for x, y in zip(list1, list2) if x % 3 != 0], key=lambda pair: pair[0] + pair[1], reverse=True)