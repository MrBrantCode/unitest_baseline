"""
QUESTION:
Write a function called `reverse_and_remove_duplicates` that takes a list of integers as input and returns a new list with the elements in reverse order and removes any duplicate elements. The function must have a time complexity of O(n), where n is the length of the input list.
"""

def entrance(lst):
    seen = set()
    result = []
    for num in reversed(lst):
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result