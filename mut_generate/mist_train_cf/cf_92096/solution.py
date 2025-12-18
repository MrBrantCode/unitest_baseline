"""
QUESTION:
Create a function called `get_next_element` that takes a list as an argument and returns the second element in the list, or None if the list is empty or contains only one element. The function should not modify the original list and should be able to handle lists of any data type. The time complexity of the function should be O(1).
"""

def get_next_element(lst):
    if len(lst) <= 1:
        return None
    return lst[1]