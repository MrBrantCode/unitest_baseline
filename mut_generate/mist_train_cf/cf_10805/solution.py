"""
QUESTION:
Write a function `compare_lists` that takes two lists `list1` and `list2` as input and returns `True` if they have the same contents in the same order, and `False` otherwise. The function should be case-sensitive and consider the data type of each element, so that for example, the integer 1 and the float 1.0 are not considered equal. The function should not use any built-in functions that directly compare lists.
"""

def compare_lists(list1, list2):
    # Check if the lengths of the lists are the same
    if len(list1) != len(list2):
        return False
    
    # Check if each element in list1 exists in list2 in the same order
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True