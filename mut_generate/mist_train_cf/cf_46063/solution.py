"""
QUESTION:
Write a function named `sort_tuples` that takes a list of integer tuples as input and returns a list of tuples sorted in descending order based on the second element of each tuple.
"""

def entrance(lst):
    return sorted(lst, key=lambda t: t[1], reverse=True)