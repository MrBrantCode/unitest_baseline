"""
QUESTION:
Implement a function `getListElement(lst, index)` that returns the element at the given index in a list. If the index is out of the list's range, return the error message 'Error: list index out of range.' without using try-except clause, instead utilizing conditional statements and recursion if necessary.
"""

def getListElement(lst, index):
    if index >= len(lst):
        return 'Error: list index out of range.'
    else:
        return lst[index]