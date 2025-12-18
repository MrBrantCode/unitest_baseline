"""
QUESTION:
Write a function called `quick_sort` to sort a list of elements in ascending order. The function should take one argument, a list of elements that can be compared using the less-than operator. The function should return the sorted list. The function should have a time complexity of O(nlogn) on average.
"""

def quick_sort(lst):
    """
    Sorts a list of elements in ascending order using the Quick Sort algorithm.

    Args:
        lst (list): A list of elements that can be compared using the less-than operator.

    Returns:
        list: The sorted list.
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)