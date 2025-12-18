"""
QUESTION:
Write a function `is_descending_alphabetical_order` that takes a list of strings as input and returns `True` if the list is in alphabetically descending order, and `False` otherwise.
"""

def is_descending_alphabetical_order(lst):
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            return False
    return True