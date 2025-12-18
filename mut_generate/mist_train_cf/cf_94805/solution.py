"""
QUESTION:
Write a function named `compare_lists` that compares two given lists and returns True if their contents are the same and in the same order, and False otherwise. The function should have a time complexity of O(n) and use constant space, where n is the length of the lists.
"""

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True