"""
QUESTION:
Write a function named `are_all_elements_equal` that takes a list of integers as input and returns True if all elements in the list are equal, False otherwise. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list. The list can contain positive or negative integers, and it may be empty.
"""

def are_all_elements_equal(lst):
    if not lst:
        return True
    first_element = lst[0]
    for element in lst:
        if element != first_element:
            return False
    return True