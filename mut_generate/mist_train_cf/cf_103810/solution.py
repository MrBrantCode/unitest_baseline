"""
QUESTION:
Write a function called `merge_lists` that takes two sorted lists of numbers as input, merges them into one sorted list, removes any duplicates, and handles cases where one or both of the lists contain negative numbers. The function should return the merged list.
"""

def merge_lists(list1, list2):
    merged_list = list(set(list1 + list2))
    return sorted(merged_list)