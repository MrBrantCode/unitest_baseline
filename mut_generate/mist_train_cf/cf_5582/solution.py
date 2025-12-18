"""
QUESTION:
Implement a function named remove_duplicates_and_sort that takes a list of integers as input and returns a new list with all duplicated entries removed and the remaining numbers sorted in descending order. The input list can contain up to 10^6 elements. The integers in the input list will have a value between -10^9 and 10^9, and the list may be empty or contain negative integers and duplicate entries.
"""

def remove_duplicates_and_sort(num_list):
    unique_nums = set(num_list)
    sorted_nums = sorted(unique_nums, reverse=True)
    return sorted_nums