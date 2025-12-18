"""
QUESTION:
Write a function `check_sort_order` that determines whether a given list is sorted in ascending or descending order, or if it's not sorted. The function should be able to handle lists containing different data types and should return one of the following strings: 'Ascending', 'Descending', 'Not sorted', or 'Empty list' if the input list is empty. The list can contain any type of elements that can be compared using the `<` and `>` operators, but it should not contain `None` values.
"""

def check_sort_order(lst):
    if not lst:  
        return 'Empty list'
    if all(prev <= curr for prev, curr in zip(lst, lst[1:])):
        return 'Ascending'
    elif all(prev >= curr for prev, curr in zip(lst, lst[1:])):
        return 'Descending'
    else:
        return 'Not sorted'