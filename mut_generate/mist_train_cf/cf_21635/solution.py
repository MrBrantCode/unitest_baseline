"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input and returns a new list containing the unique elements from the input list. The function should have a time complexity of O(n), where n is the length of the list, and must not use any built-in Python functions or methods that directly delete or remove elements from a list.
"""

def remove_duplicates(lst):
    unique_elements = []
    for num in lst:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements