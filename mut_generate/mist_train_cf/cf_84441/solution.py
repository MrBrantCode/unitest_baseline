"""
QUESTION:
Create a function named `sort_tuples_by_second` that takes a list of tuples as input and returns the sorted list based on the length of the second element in each tuple. The function should sort the list in-place and in ascending order. The list must only contain tuples with at least two elements.
"""

def sort_tuples_by_second(list_of_tuples):
    # Sort the list in place using the length of the second element in each tuple as the key
    list_of_tuples.sort(key=lambda x: len(x[1]))
    return list_of_tuples