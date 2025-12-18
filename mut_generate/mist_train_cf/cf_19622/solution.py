"""
QUESTION:
Create a function named sort_list that takes a list of tuples as input. Sort the list in ascending order based on the sum of the absolute values of the elements in each tuple. If two tuples have the same sum, sort them based on the second element in descending order.
"""

def sort_list(lst):
    return sorted(lst, key=lambda x: (sum(abs(i) for i in x), -x[1]))