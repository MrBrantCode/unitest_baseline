"""
QUESTION:
Write a function named `intersection` that takes two lists of integers as input and returns a new list containing the common elements found in both input lists, without duplicates and in the same order as they appear in the first list. The function should not use any built-in set operations or other Python functions that directly compute the intersection of lists.
"""

def intersection(lst1, lst2):
    result = []
    for i in lst1:
        if i in lst2 and i not in result:
            result.append(i)
    return result