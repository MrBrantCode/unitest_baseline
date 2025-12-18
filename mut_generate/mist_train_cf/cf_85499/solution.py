"""
QUESTION:
Write a function called `symmetric_difference` that takes two lists of elements as input and returns a list of elements that are in exactly one of the input lists. The function should have a time complexity of O(n), where n is the total number of elements in both lists.
"""

def symmetric_difference(arr_1, arr_2):
    set_1 = set(arr_1)
    set_2 = set(arr_2)
    return list((set_1 - set_2) .union(set_2 - set_1))