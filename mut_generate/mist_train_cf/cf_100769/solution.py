"""
QUESTION:
Write a function called `sort_and_remove_duplicates` that takes a list of integers as input, removes any duplicates, and returns the resulting list sorted in descending order. The function should return the sorted list of integers with duplicates removed. The function should run in a reasonable time complexity.
"""

def sort_and_remove_duplicates(lst):
    # convert list to set to remove duplicates, then back to list
    unique_lst = list(set(lst))
    # sort list in descending order
    sorted_lst = sorted(unique_lst, reverse=True)
    return sorted_lst