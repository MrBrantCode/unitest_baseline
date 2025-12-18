"""
QUESTION:
Write a function `split_list(lst, n)` that takes a list `lst` of items and a prime number `n` as input. The function should return a list of tuples, where each tuple represents a group of `n` items from the input list. The function should handle the following conditions: 
- If the input list is empty, it should return an empty list.
- If the input list has duplicate items, they should be removed before splitting into groups.
- The input list can contain any type of items, not necessarily integers or strings.
"""

def split_list(lst, n):
    """
    Split a list into groups of n items, removing duplicates and handling empty lists.

    Args:
    lst (list): The input list to be split.
    n (int): The number of items in each group.

    Returns:
    list: A list of tuples, each containing n items from the input list.
    """
    unique_lst = list(set(lst))
    if len(unique_lst) == 0:
        return []
    
    groups = []
    for i in range(0, len(unique_lst), n):
        group = tuple(unique_lst[i:i+n])
        groups.append(group)
    
    return groups