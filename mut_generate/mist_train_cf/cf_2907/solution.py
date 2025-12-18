"""
QUESTION:
Implement a function named `get_unique_elements` that takes a list of integers as input and returns a new list containing only the unique elements, in the order they appeared in the original list, removing any duplicates that occur consecutively. The function should have a time complexity of O(n) and should not use any built-in library functions or data structures.
"""

def get_unique_elements(lst):
    unique_lst = []
    prev = None
    for num in lst:
        if num != prev:
            unique_lst.append(num)
        prev = num
    return unique_lst