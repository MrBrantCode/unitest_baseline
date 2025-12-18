"""
QUESTION:
Create a function `merge_lists` that takes two lists of integers as input. The function should merge the two lists by combining all elements, sort the merged list in ascending order, remove any duplicate elements, and filter out numbers that are not divisible by 3. The function should return the resulting list of integers.
"""

def merge_lists(list1, list2):
    """
    Merge two lists of integers, sort the merged list in ascending order, 
    remove any duplicate elements, and filter out numbers that are not divisible by 3.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        list: The resulting list of integers.
    """
    merged_list = list(set(list1 + list2))
    merged_list.sort()
    
    return [x for x in merged_list if x % 3 == 0]