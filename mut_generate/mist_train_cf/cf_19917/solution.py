"""
QUESTION:
Write a function `contains_duplicates` that takes a list of integers as input and returns a boolean indicating whether the list contains any duplicate elements. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list. The list may contain both positive and negative integers.
"""

def contains_duplicates(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return True
        seen.add(num)
    return False