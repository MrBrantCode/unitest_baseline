"""
QUESTION:
Create a function named `longest_sublist` that takes a list of lists as input. The function should return a tuple containing the length of the longest sublist and the index of the first occurrence of this longest sublist in the list of lists. If there are multiple sublists with the same maximum length, return the index of the first one encountered.
"""

def longest_sublist(lst):
    max_length = max(len(sublist) for sublist in lst)
    index_of_longest = next(i for i, sublist in enumerate(lst) if len(sublist) == max_length)
    return (max_length, index_of_longest)