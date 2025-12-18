"""
QUESTION:
Write a function `contains_duplicates` that takes a list of integers as input and returns `True` if the list contains duplicates and `False` otherwise. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the list. The input list can contain both positive and negative integers.
"""

def contains_duplicates(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return True
        seen.add(num)
    return False