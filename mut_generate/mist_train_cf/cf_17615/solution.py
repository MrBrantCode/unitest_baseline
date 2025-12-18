"""
QUESTION:
Write a function named `compare_lists` that takes two lists as input and returns `True` if the lists have the same contents in the same order, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the lists, and use constant space.
"""

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True