"""
QUESTION:
Create a function `select_kth_smallest(lst, k)` to find the kth smallest item in a list. The function should have a time complexity of O(log n) and a space complexity of O(log n). The function must use a recursive approach. The value of k is between 1 and the length of the list.
"""

def select_kth_smallest(lst, k):
    """
    Find the kth smallest item in a list using a recursive approach.

    Args:
        lst (list): The input list.
        k (int): The index of the desired item (1-indexed).

    Returns:
        The kth smallest item in the list.
    """
    if len(lst) == 1:
        return lst[0]
    
    pivot = lst[len(lst)//2]
    smaller = [x for x in lst if x < pivot]
    equal = [x for x in lst if x == pivot]
    larger = [x for x in lst if x > pivot]
    
    if k <= len(smaller):
        return select_kth_smallest(smaller, k)
    elif k <= len(smaller) + len(equal):
        return equal[0]
    else:
        return select_kth_smallest(larger, k - len(smaller) - len(equal))