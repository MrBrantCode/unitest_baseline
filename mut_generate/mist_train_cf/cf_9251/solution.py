"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of integers as input, and returns a new list with duplicate elements removed while maintaining the original order of elements.
"""

def remove_duplicates(lst):
    new_list = []
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    return new_list