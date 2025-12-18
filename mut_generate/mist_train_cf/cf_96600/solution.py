"""
QUESTION:
Write a function `complement_list(lst)` that takes a list of binary integers as input and returns the list with all elements replaced by their complement (1 - element). The function should not use any built-in functions or methods. It must have a time complexity of O(n), where n is the length of the list, and a space complexity of O(1).
"""

def complement_list(lst):
    for i in range(len(lst)):
        lst[i] = 1 - lst[i]
    return lst