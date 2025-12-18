"""
QUESTION:
Write a function named `reverse_and_remove_duplicates` that takes a list of integers as input and returns a new list with the elements in reverse order and no duplicates. The function must have a time complexity of O(n), where n is the length of the input list.
"""

def reverse_and_remove_duplicates(input_list):
    seen = set()
    result = []
    for num in reversed(input_list):
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result