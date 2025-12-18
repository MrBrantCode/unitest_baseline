"""
QUESTION:
Write a function called `remove_duplicates_and_sort_desc` that takes a list of integers as input, removes duplicates from the list, sorts the remaining items in descending order, and returns the result as a new list.
"""

def remove_duplicates_and_sort_desc(input_list):
    return sorted(list(set(input_list)), reverse=True)