"""
QUESTION:
Write a function `are_all_elements_equal(lst)` that checks if all elements in a list are equal. The list can contain positive or negative integers. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.
"""

def are_all_elements_equal(lst):
    if not lst:
        return True
    first_element = lst[0]
    for element in lst:
        if element != first_element:
            return False
    return True