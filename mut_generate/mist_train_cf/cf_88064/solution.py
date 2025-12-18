"""
QUESTION:
Write a function named `check_all_equal` that takes a list of up to 100 elements, each of which can be either an integer or a string of up to 50 characters, as input. The function should return True if all elements in the list are equal, regardless of type, and False otherwise. If the input list is empty, the function should return False. The function should have a time complexity of O(n), where n is the number of elements in the list.
"""

def check_all_equal(lst):
    if len(lst) == 0:
        return False

    first_element = lst[0]
    for element in lst:
        if element != first_element:
            return False

    return True