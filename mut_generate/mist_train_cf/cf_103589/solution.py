"""
QUESTION:
Write a function `compact_list` that takes a list as input and returns a new list containing unique items from the input list in the original order. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list. The implementation should not use any built-in Python functions or libraries for dictionary or list manipulation.
"""

def compact_list(given_list):
    compact_dict = {}
    compact_list = []
    
    for item in given_list:
        if item not in compact_dict:
            compact_dict[item] = True
            compact_list.append(item)
    
    return compact_list