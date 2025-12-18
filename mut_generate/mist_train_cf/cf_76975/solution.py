"""
QUESTION:
Write a function named 'is_ascending_order' that takes a list of integers as input and returns True if the list is in ascending order (smallest to largest) and False otherwise.
"""

def is_ascending_order(lst):
    return lst == sorted(lst)