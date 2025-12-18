"""
QUESTION:
Combine two lists into a single list with no duplicates and sort it in ascending order. 

Write a function `combine_and_sort_lists(list_first, list_second)` that takes two lists as input and returns a new sorted list containing all unique elements from both lists. The time complexity of the solution should be O(n log n), where n is the total number of elements in both lists.
"""

def combine_and_sort_lists(list_first, list_second):
    # Combine the two lists into a single list
    combined_list = list_first + list_second

    # Remove duplicates from the combined list
    combined_list = list(set(combined_list))

    # Sort the combined list in ascending order
    combined_list.sort()

    return combined_list