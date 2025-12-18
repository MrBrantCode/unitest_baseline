"""
QUESTION:
Write a function `sort_and_remove_duplicates` that takes a list of integers as input, removes duplicates, and returns a new list with the remaining integers sorted in descending order.
"""

def sort_and_remove_duplicates(lst):
    # convert list to set to remove duplicates, then back to list
    unique_lst = list(set(lst))
    # sort list in descending order
    sorted_lst = sorted(unique_lst, reverse=True)
    return sorted_lst