"""
QUESTION:
Write a function `get_unique_elements(lst)` that takes a list of integers as input and returns a list containing only the unique elements from the original list. The function must have a time complexity of O(n) and a space complexity of O(1), without using any built-in functions or libraries for counting or checking for uniqueness.
"""

def entrance(lst):
    unique_elements = []
    for element in lst:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements