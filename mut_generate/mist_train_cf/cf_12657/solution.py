"""
QUESTION:
Write a function named `same_items_in_different_order` that takes two lists as input and returns `True` if they contain the same items in different order, and `False` otherwise. The function must have a time complexity of O(n log n), where n is the length of the lists. The function should assume that the input lists contain elements that can be compared using the `==` operator and that can be sorted using the `sort()` method.
"""

def same_items_in_different_order(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    return list1 == list2