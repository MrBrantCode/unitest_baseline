"""
QUESTION:
Write a function `split_list_into_groups` that takes a list of items and an integer `n` as input, where `n` is a prime number. The function should return a list of tuples, where each tuple represents a group of `n` items from the input list. If the length of the list is not a multiple of `n`, the last group should contain the remaining items.
"""

def split_list_into_groups(lst, n):
    """
    Splits a list into groups of size n.

    Args:
        lst (list): The input list to be split.
        n (int): The size of each group.

    Returns:
        list: A list of tuples, where each tuple represents a group of n items from the input list.
    """
    return [tuple(lst[i:i+n]) for i in range(0, len(lst), n)]