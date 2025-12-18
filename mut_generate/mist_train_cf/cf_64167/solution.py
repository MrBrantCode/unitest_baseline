"""
QUESTION:
Write a function named `sort_tuple` that accepts a list of tuples as input, where each tuple consists of an integer and a nested tuple of integers. The function should return a list of tuples sorted by the second element of the nested tuple in descending order.
"""

def sort_tuple(lst):
    return sorted(lst, key = lambda x: x[1][1], reverse=True)