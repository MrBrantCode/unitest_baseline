"""
QUESTION:
Write a function named `remove_duplicates_and_sort_desc` that takes a list of integers as input, removes duplicates, and returns the remaining numbers in descending order. The function should have a time complexity of O(n log n) or better and be able to handle lists with up to 10^6 elements.
"""

def remove_duplicates_and_sort_desc(num_list):
    return sorted(list(set(num_list)), reverse=True)