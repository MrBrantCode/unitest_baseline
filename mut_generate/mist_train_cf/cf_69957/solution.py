"""
QUESTION:
Write a function `remove_duplicates_sort_desc(lst)` that takes a list of elements as input, removes successive identical elements, and returns a new list with the remaining elements sorted in descending order. The function should be able to handle both numerical and alphabetical elements. If the list contains a mix of numbers and strings, they should be sorted as if they were all strings. The input list is not guaranteed to be sorted.
"""

from itertools import groupby

def remove_duplicates_sort_desc(lst):
    lst.sort(key=str)  # sort list before using groupby
    no_duplicates = [key for key, _ in groupby(lst)]
    return sorted(no_duplicates, key=str, reverse=True)