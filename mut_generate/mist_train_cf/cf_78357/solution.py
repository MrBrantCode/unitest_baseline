"""
QUESTION:
Write a function named `removeDuplicates` that takes a list as input and returns a new list containing the same elements in the same order, but with duplicates removed. The input list can contain elements of any type. Do not use any built-in or external library functions for removing duplicates.
"""

def removeDuplicates(lst):
    no_duplicates = []
    for element in lst:
        if element not in no_duplicates:
            no_duplicates.append(element)
    return no_duplicates