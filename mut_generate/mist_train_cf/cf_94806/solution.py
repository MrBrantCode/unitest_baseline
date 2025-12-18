"""
QUESTION:
Create a function named `remove_duplicates` that takes a list as input and returns a new list containing unique elements from the original list, maintaining their original order. The function should not use any built-in functions for removing duplicates and should have a time complexity of O(n), where n is the length of the input list.
"""

def entance(lst):
    unique_lst = []
    seen = set()

    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)

    return unique_lst