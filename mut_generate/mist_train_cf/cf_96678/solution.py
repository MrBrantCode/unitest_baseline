"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique elements from the input list. The function should have a time complexity of O(n), where n is the length of the input list, and should not use built-in Python functions or methods that directly delete or remove elements from a list. The order of the elements in the output does not matter, and the input list may contain negative integers and may be empty.
"""

def remove_duplicates(lst):
    unique_elements = []
    for num in lst:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements