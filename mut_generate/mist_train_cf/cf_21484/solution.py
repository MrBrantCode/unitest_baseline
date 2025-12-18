"""
QUESTION:
Write a function `complement_list(lst)` that takes a list of binary numbers (0s and 1s) as input, and returns the complement of the given list. The function should not use any built-in functions or methods. The time complexity of the function should be O(n) and the space complexity should be O(1), where n is the length of the list.
"""

def complement_list(lst):
    for i in range(len(lst)):
        lst[i] = 1 - lst[i]
    
    return lst