"""
QUESTION:
Write a function named compare_lists that takes two lists as input, compares them, and prints whether they are equal or not. The function should consider the order of elements in the lists and handle nested lists by comparing them recursively. The lists can contain integers, strings, or a combination of both. The function should have a time complexity of O(n), where n is the length of the longer list, and a space complexity of O(1).
"""

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if type(list1[i]) != type(list2[i]):
            return False
        
        if isinstance(list1[i], list) and isinstance(list2[i], list):
            if not compare_lists(list1[i], list2[i]):
                return False
        
        elif list1[i] != list2[i]:
            return False
    
    return True