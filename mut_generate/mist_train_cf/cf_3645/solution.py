"""
QUESTION:
Write a function named `check_all_equal` that checks if all elements in the input list are equal. The function should handle cases where the input list contains both integers and strings, with a maximum length of 50 characters, and can include uppercase and lowercase letters and special characters. The function should return True if all elements are equal and False otherwise. If the input list is empty, the function should return False. The time complexity of the function should be O(n), where n is the number of elements in the list, which should not exceed 100.
"""

def entrance(lst):
    if len(lst) == 0:
        return False

    first_element = lst[0]
    for element in lst:
        if element != first_element:
            return False

    return True