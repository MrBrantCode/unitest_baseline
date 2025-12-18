"""
QUESTION:
Create a function named `sort_tuples` that takes a list of tuples as input. Each tuple contains two elements. The function should sort the list of tuples based on the length of the second element in each tuple and return the sorted list. The function should sort in ascending order by default, but it should be possible to modify it to sort in descending order if needed.
"""

def sort_tuples(list_of_tuples):
    sorted_tuples = sorted(list_of_tuples, key=lambda x: len(x[1]))
    return sorted_tuples