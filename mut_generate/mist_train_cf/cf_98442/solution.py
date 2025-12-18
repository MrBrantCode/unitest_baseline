"""
QUESTION:
Write a function named `sort_and_remove_duplicates` that takes a list of integers as input, removes duplicates, and returns the list sorted in descending order. The function should have a time complexity of O(n log n) or better.
"""

def sort_and_remove_duplicates(lst):
    # convert list to set to remove duplicates, then back to list
    unique_lst = list(set(lst))
    # sort list in descending order
    sorted_lst = sorted(unique_lst, reverse=True)
    return sorted_lst