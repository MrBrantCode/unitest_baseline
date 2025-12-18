"""
QUESTION:
Create a function `find_unique_elements` that takes a list of integers as input and returns a new list containing only the unique elements in the order they first appeared in the input list. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list. Implement the function without using built-in Python functions or data structures such as sets or dictionaries.
"""

def find_unique_elements(lst):
    unique_lst = []
    seen_elements = []

    for element in lst:
        if element not in seen_elements:
            unique_lst.append(element)
            seen_elements.append(element)

    return unique_lst