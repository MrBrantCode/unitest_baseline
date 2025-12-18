"""
QUESTION:
Create a Python class called `SortedList` that maintains an ordered list with methods to add and remove elements while ensuring the list remains sorted. The class should include an `add` method to insert an element into the list, a `remove` method to delete an element, and a `display` method to return the sorted list.
"""

import bisect 

def entance(lst, element):
    bisect.insort(lst, element)
    return lst

def remove(lst, element):
    if element in lst:
        lst.remove(element)
    return lst