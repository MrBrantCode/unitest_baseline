"""
QUESTION:
Write a function `sort_list_with_duplicates` that takes a list of integers `given_list` and a string `sort_order` as input, and returns a sorted list of unique integers. The list should be sorted in ascending order if `sort_order` is "ascending", and in descending order if `sort_order` is "descending". The function should have a time complexity of O(nlogn).
"""

def sort_list_with_duplicates(given_list, sort_order):
    sorted_list = sorted(set(given_list))
    if sort_order == "descending":
        sorted_list.reverse()
    return sorted_list