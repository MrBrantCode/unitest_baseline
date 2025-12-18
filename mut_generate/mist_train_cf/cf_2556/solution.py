"""
QUESTION:
Create a function named `combine_and_sort_lists` that takes two lists of integers as input. The function should combine these lists into a single list, remove any duplicates, and sort the resulting list in ascending order. The solution should have a time complexity of O(n log n), where n is the total number of elements in both lists. The function should return the sorted list.
"""

def combine_and_sort_lists(list_first, list_second):
    # Combine the two lists into a single list
    combined_list = list_first + list_second

    # Remove duplicates from the combined list
    combined_list = list(set(combined_list))

    # Sort the combined list in ascending order
    combined_list.sort()

    return combined_list